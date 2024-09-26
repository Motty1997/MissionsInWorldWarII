from returns.maybe import Maybe
from config.base import session_factory
from models import Country


def find_country_by_id(c_id: int) -> Maybe[Country]:
    with session_factory() as session:
        return Maybe.from_optional(session.get(Country, c_id))
