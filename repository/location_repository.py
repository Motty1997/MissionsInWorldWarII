from returns.maybe import Maybe
from config.base import session_factory
from models import Location


def find_location_by_id(l_id: int) -> Maybe[Location]:
    with session_factory() as session:
        return Maybe.from_optional(session.get(Location, l_id))
