from typing import Dict
from sqlalchemy import inspect
from models import Target


def convert_to_json(target: Target) -> Dict[str, str]:
    return {c.key: getattr(target, c.key) for c in inspect(target).mapper.column_attrs}
