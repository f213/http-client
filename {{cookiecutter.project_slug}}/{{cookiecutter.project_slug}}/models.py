from dataclasses import dataclass
from dataclasses import fields
from datetime import datetime
from typing import Union

from {{cookiecutter.project_slug}}.helpers import snakesify_dict_keys


class Deserializers:
    """Convert fields to python"""
    @staticmethod
    def string_bool_to_bool(value: Union[str, bool]) -> bool:
        if isinstance(value, bool):
            return value

        return value.lower() == 'true'

    @staticmethod
    def datetime(value):
        return datetime.fromisoformat(value)


class Serializers:
    """Convert fields from python to JSON"""
    @staticmethod
    def noop(value):
        return value

    @staticmethod
    def dropper(value):
        return '__dropped__'

    @staticmethod
    def default(value):
        if value is None or isinstance(value, bool):
            return value

        return str(value)


@dataclass
class Model:
    """Base class for wildberries items, converting their non-formatted stuff to python data"""

    def to_json(self) -> dict:
        result = dict()
        for field in fields(self):
            result.update(self.serialize(field))

        return result

    @classmethod
    def from_json(cls, data: Union[list, dict]):
        """Make a dataclass instance out of vendor dump"""
        initial_raw_data = data

        line = snakesify_dict_keys(data)

        result = dict()
        for field in fields(cls):
            field_name = cls.get_field_name(field)  # if field has defined custom source

            value = cls.deserialize(field=field, value=line.get(field_name))

            result[field.name] = value

        if cls.has_field('initial_raw_data'):
            result['initial_raw_data'] = initial_raw_data

        return cls(**result)

    @classmethod
    def has_field(cls, name) -> bool:
        return name in [field.name for field in fields(cls)]

    @staticmethod
    def deserialize(value, field):
        """Convert field if deserializer is specified"""
        if 'deserializer' in field.metadata:
            return field.metadata['deserializer'](value)

        return value

    @staticmethod
    def get_field_name(field) -> str:
        """If field has defined source field name, return it"""
        return field.metadata.get('source', field.name)

    def serialize(self, field) -> dict:
        key = field.metadata.get('destination', field.name)  # if we have destination name -- use it, otherwise use field name

        serializer = field.metadata['serializer'] if 'serializer' in field.metadata else Serializers.default

        field_value = getattr(self, field.name)
        serialized = serializer(field_value)

        if serialized != '__dropped__':
            return {key: serializer(field_value)}

        return ''
