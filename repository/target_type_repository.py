from returns.maybe import Maybe
from config.base import session_factory
from models import TargetType


def find_target_type_by_id(tt_id: int) -> Maybe[TargetType]:
    with session_factory() as session:
        return Maybe.from_optional(session.get(TargetType, tt_id))
