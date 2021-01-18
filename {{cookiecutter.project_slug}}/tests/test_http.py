import pytest

from {{cookiecutter.project_slug}}.http import HTTPException


@pytest.mark.parametrize('url', [
    'v1/suppliers/orders',
    '/v1/suppliers/orders',
    '/v1/suppliers/orders/',
])
def test_200(client, url, httpx_mock):
    httpx_mock.add_response(
        method='GET',
        url='https://host.io/api/v1/suppliers/orders',
        json={'__mocked': True},
    )

    assert client.http.get(url) == {'__mocked': True}


@pytest.mark.parametrize(
    ('code', 'exception'), [
        (404, HTTPException),
        (503, HTTPException),
    ],
)
def test_error(client, code, exception, httpx_mock):
    httpx_mock.add_response(
        status_code=code,
        json={'__mocked': True},
    )

    with pytest.raises(exception):
        client.http.get('v1/suppliers/orders')
