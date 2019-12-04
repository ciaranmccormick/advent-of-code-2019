from main import calculate_required_fuel, calculate_total_fuel
import unittest


class DayOneTest(unittest.TestCase):
    def test_calculate_fuel(self):
        inputs = [(12, 2), (14, 2), (1969, 654), (100756, 33583)]
        for data in inputs:
            with self.subTest(data=data):
                self.assertEqual(data[1], calculate_required_fuel(data[0]))

    def test_calculate_fuel_fuel(self):
        inputs = [(14, 2), (1969, 966), (100756, 50346)]
        for data in inputs:
            with self.subTest(data=data):
                self.assertEqual(data[1], calculate_total_fuel(data[0]))


if __name__ == "__main__":
    unittest.main()
