from typing import List, Dict
from sqlalchemy import text
from returns.maybe import Nothing, Maybe
from returns.result import Result, Failure, Success
from sqlalchemy.exc import SQLAlchemyError
from config.base import session_factory
from models import Target
from repository.city_repository import find_city_by_id
from repository.location_repository import find_location_by_id
from repository.target_type_repository import find_target_type_by_id
from service.target_service import convert_to_json


def insert_target(target: Target) -> Result[Target, str]:
    with session_factory() as session:
        try:
            maybe_city = find_city_by_id(target.sity_id).map(session.merge)
            maybe_target_type = find_target_type_by_id(target.target_type_id).map(session.merge)
            maybe_location = find_location_by_id(target.location_id).map(session.merge)

            if any(entity is Nothing for entity in [maybe_city, maybe_target_type, maybe_location]):
                return Failure("Missing entity of target")

            maybe_target_industry = Maybe(target.target_industry)
            maybe_target_priority = Maybe(target.target_priority)

            if maybe_target_industry.is_nothing():
                return Failure("target_industry is missing")
            if maybe_target_priority.is_nothing():
                return Failure("target_priority is missing")

            target.city_id = maybe_city.unwrap()
            target.target_type_id = maybe_target_type.unwrap()
            target.location_id = maybe_location.unwrap()
            target.target_industry = maybe_target_industry.unwrap()
            target.target_priority = maybe_target_priority.unwrap()
            session.add(target)
            session.commit()
            session.refresh(target)
            return Success(target)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))

def find_target_by_id(t_id: int) -> Maybe[Target]:
    with session_factory() as session:
        return Maybe.from_optional(session.get(Target, t_id))

def delete_target_by_id(t_id: int) -> Result[Target, str]:
    with session_factory() as session:
        try:
            maybe_target = find_target_by_id(t_id).map(session.merge)
            if maybe_target is Nothing:
                return Failure(f"No target under the id {t_id}")
            target = maybe_target.unwrap()
            session.delete(target)
            session.commit()
            return Success(target)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))

def update_target(t_id: int, target: Target) -> Result[Target, str]:
    with session_factory() as session:
        try:
            maybe_rental = find_target_by_id(t_id).map(session.merge)
            if maybe_rental is Nothing:
                return Failure(f"No rental under the id {t_id}")
            target_to_update = maybe_rental.unwrap()
            target_to_update.late_fee = target.late_fee
            target_to_update.rental_fee = target.rental_fee
            target_to_update.return_date = target.return_date
            target_to_update.rental_date = target.rental_date
            session.commit()
            session.refresh(target_to_update)
            return Success(target_to_update)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))


def find_all_targets() -> List[Dict[str, str]]:
    with session_factory() as session:
        result = session.execute(text('SELECT * FROM targets;'))
        res = result.fetchall()
        targets = [convert_to_json(Target(**dict(row._mapping))) for row in res]
        return targets
