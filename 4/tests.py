import pytest

from main import (
    always_increases,
    contains_more_than_two_repeats,
    contains_two_repeats_only,
    contains_repeats,
)


@pytest.mark.parametrize(
    "test_input,expected",
    [("123456", False), ("1123456", True), ("123445", True), ("123455", True),],
)
def test_contains_repeats(test_input, expected):
    assert expected == contains_repeats(test_input)


@pytest.mark.parametrize(
    "test_input,expected",
    [("123456", True), ("1123456", True), ("126445", False), ("123451", False)],
)
def test_always_increasing(test_input, expected):
    assert expected == always_increases(test_input)


@pytest.mark.parametrize(
    "test_input,expected",
    [("123456", False), ("111234", True), ("211134", True), ("123444", True),],
)
def test_contains_more_than_two_repeats(test_input, expected):
    assert expected == contains_more_than_two_repeats(test_input)


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("123456", False),
        ("111234", False),
        ("211144", True),
        ("123444", False),
        ("123245", False),
    ],
)
def test_contains_two_repeats_only(test_input, expected):
    assert expected == contains_two_repeats_only(test_input)
