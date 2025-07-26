from sqlalchemy.types import TypeDecorator, TEXT
import json

class Config(TypeDecorator):
    impl = TEXT
    cache_ok = True

class StringList(Config):
    def process_bind_param(self, value, dialect):
        if value is None:
            return "[]"
        return json.dumps(value)

    def process_result_value(self, value, dialect):
        if not value:
            return []
        return json.loads(value)

class IntList(Config):
    def process_bind_param(self, value, dialect):
        return json.dumps(value or [])

    def process_result_value(self, value, dialect):
        return json.loads(value or "[]")


class JSONDict(Config):
    def process_bind_param(self, value, dialect):
        if value is None:
            return "{}"
        return json.dumps(value)

    def process_result_value(self, value, dialect):
        if not value:
            return {}
        return json.loads(value)