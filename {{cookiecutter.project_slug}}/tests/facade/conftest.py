import pytest


@pytest.fixture
def http_get(mocker):
    return mocker.patch('{{cookiecutter.project_slug}}.http.HTTP.get')
