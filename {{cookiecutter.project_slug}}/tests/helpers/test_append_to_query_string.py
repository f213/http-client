import pytest

from {{cookiecutter.project_slug}}.helpers import append_to_query_string


@pytest.mark.parametrize(
    ('data', 'expected'),
    [
        (
            {'key': 'lol', 'value': 'kek', 'url': 'https://tst.hst/'},
            'https://tst.hst/?lol=kek',
        ),
        (
            {'key': 'lol', 'value': 'kek', 'url': 'https://tst.hst/?lol1=kek1'},
            'https://tst.hst/?lol1=kek1&lol=kek',
        ),
        (
            {'key': 'lol', 'value': 'kek', 'url': 'https://tst.hst/?kek=lol'},
            'https://tst.hst/?kek=lol&lol=kek',
        ),
    ],
)
def test(data, expected):
    assert append_to_query_string(**data) == expected
