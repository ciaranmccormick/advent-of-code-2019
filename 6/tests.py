import pytest

from main import (
    Orbit,
    get_direct_orbit,
    get_indirect_orbits,
    get_total_orbits,
    get_total_map_orbits,
    moves_between_orbits,
    get_first_common_orbit,
    number_of_transfers,
)

test_input = """
COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
"""

addition_input = """
K)YOU
I)SAN
"""


def get_test_orbits():
    test_orbits = [
        Orbit(*line.split(")")) for line in test_input.split("\n") if not line == ""
    ]
    return test_orbits


def get_additional_orbits():
    string = test_input + addition_input
    test_orbits = [
        Orbit(*line.split(")")) for line in string.split("\n") if not line == ""
    ]
    return test_orbits


@pytest.mark.parametrize("test_input,expected", [("D", "C"), ("L", "K"), ("COM", None)])
def test_build_map(test_input, expected):
    orbits = get_test_orbits()
    assert expected == get_direct_orbit(test_input, orbits)


@pytest.mark.parametrize(
    "test_input,expected",
    [("D", ["B", "COM"]), ("L", ["J", "E", "D", "C", "B", "COM"]), ("COM", [])],
)
def test_get_indirect_orbits(test_input, expected):
    orbits = get_test_orbits()
    assert expected == get_indirect_orbits(test_input, orbits)


@pytest.mark.parametrize("test_input,expected", [("D", 3), ("L", 7), ("COM", 0)])
def test_get_total_orbits(test_input, expected):
    orbits = get_test_orbits()
    assert expected == get_total_orbits(test_input, orbits)


def test_get_total_map_orbits():
    orbits = get_test_orbits()
    assert 42 == get_total_map_orbits(orbits)


def test_additional_input():
    orbits = get_additional_orbits()
    assert "K" == get_direct_orbit("YOU", orbits)
    assert "I" == get_direct_orbit("SAN", orbits)


def test_moves_between_orbits():
    orbits = get_additional_orbits()
    assert 3 == moves_between_orbits("YOU", "D", orbits)
    assert 1 == moves_between_orbits("SAN", "D", orbits)


def test_get_first_common_orbit():
    orbits = get_additional_orbits()
    assert "D" == get_first_common_orbit("YOU", "SAN", orbits)


def test_number_of_transfers():
    orbits = get_additional_orbits()
    assert 4 == number_of_transfers("YOU", "SAN", orbits)

