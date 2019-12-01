from dayone import calculate_required_fuel, calculate_total_fuel
import pytest


@pytest.mark.parametrize(
    "test_input,expected", [(12, 2), (14, 2), (1969, 654), (100756, 33583)]
)
def test_calculate_fuel(test_input, expected):
    assert expected == calculate_required_fuel(test_input)


@pytest.mark.parametrize("test_input,expected", [(14, 2), (1969, 966), (100756, 50346)])
def test_calculate_fuel_fuel(test_input, expected):
    assert expected == calculate_total_fuel(test_input)
