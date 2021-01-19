from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
import pytest

from {{cookiecutter.project_slug}}.models import Deserializers
from {{cookiecutter.project_slug}}.models import Model
from {{cookiecutter.project_slug}}.models import Serializers


@dataclass
class TstModel(Model):
    id: int = field(metadata={  # NOQA: VNE003
        'serializer': Serializers.noop,
    })
    pk: str = field(metadata={
        'source': 'id',
        'deserializer': str,
    })
    boolean: bool = field(metadata={
        'source': 'bool_field',
        'deserializer': Deserializers.string_bool_to_bool,
    })
    date: datetime = field(metadata={
        'deserializer': Deserializers.datetime,
    })
    field_to_drop: str = field(metadata={
        'source': 'bool_field',
        'serializer': Serializers.dropper,
    })
    string_bool: str = field(metadata={
        'source': 'bool_field',
    })


@pytest.fixture
def test_data():
    return {
        'id': 100500,
        'boolField': 'true',
        'date': '2032-12-01 15:30:45',
    }


@pytest.fixture
def model(test_data):
    return TstModel.from_json(test_data)


def test_field_types(model):
    assert model.id == 100500
    assert model.pk == '100500'


@pytest.mark.parametrize('initial', [True, False])
def test_boolean_fields(test_data, initial):
    test_data['boolField'] = str(initial)

    model = TstModel.from_json(test_data)

    assert model.boolean is initial
    assert model.string_bool == str(initial)


def test_no_initial_raw_data_by_default(model):
    assert not hasattr(model, 'initial_raw_data')


def test_initial_raw_data(test_data):
    @dataclass
    class ModelWithInitialRawData(TstModel):
        initial_raw_data: dict

    model = ModelWithInitialRawData.from_json(test_data)

    assert model.initial_raw_data == test_data


def test_json(model):
    json = model.to_json()

    assert json['id'] == 100500
    assert json['pk'] == '100500'
    assert json['date'] == '2032-12-01 15:30:45'
    assert 'field_to_drop' not in json
