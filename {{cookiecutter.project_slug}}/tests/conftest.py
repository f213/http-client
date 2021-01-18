import json
from os import path

import pytest

from {{cookiecutter.project_slug}} import {{cookiecutter.project_facade}}


@pytest.fixture
def client():
    return {{cookiecutter.project_facade}}(token='testing')


@pytest.fixture
def read_fixture():
    """Fixture reader"""
    def read_file(file_path):
        with open(path.join('tests/.fixtures/', file_path) + '.json') as fp:
            return json.load(fp)

    return read_file
