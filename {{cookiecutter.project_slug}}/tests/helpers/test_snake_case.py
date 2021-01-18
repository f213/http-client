import pytest

from {{cookiecutter.project_slug}}.helpers import snake_case, snakesify_dict_keys


@pytest.mark.parametrize(
    ('string', 'expected'), [
        ('a', 'a'),
        ('AA', 'a_a'),
        ('TestCase', 'test_case'),
        ('testCase', 'test_case'),
        ('incomeID', 'income_i_d'),
    ],
)
def test_snake_case(string, expected):
    assert snake_case(string) == expected


@pytest.mark.parametrize(
    ('dictionary', 'expected'), [
        ({'a': 1}, {'a': 1}),
        ({'AA': 1}, {'a_a': 1}),
        ({'a_a': 1}, {'a_a': 1}),
        ({'AA': 1, 'BB': 2}, {'a_a': 1, 'b_b': 2}),
        ({'TestCase': 1}, {'test_case': 1}),
    ],
)
def test_snakesify_dict_keys(dictionary, expected):
    assert snakesify_dict_keys(dictionary) == expected
