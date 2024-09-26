from returns.maybe import Maybe
from config.base import session_factory
from models import City


def find_city_by_id(c_id: int) -> Maybe[City]:
    with session_factory() as session:
        return Maybe.from_optional(session.get(City, c_id))
