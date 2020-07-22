import unittest
import unittest.mock
import numpy as np

from ZeroGeneration import ZeroGeneration
from NextGeneration import NextGeneration


class TestModule(unittest.TestCase):

    @unittest.mock.patch('builtins.input', side_effect=["000", "111", "000", "000"])
    def test_create_zero(self, mock):
        """Should create object successfully"""
        zero_gen = ZeroGeneration(3, 3)
        expected_result = np.array([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])

        self.assertEqual(zero_gen.zero_generation.all(), expected_result.all())

    @unittest.mock.patch('builtins.input', side_effect=["000", "111", "000", "000", "1, 0, 10"])
    def test_example_one(self, mock):
        """[0]
        Should create next generations and
        count how many times was the target green"""
        zero_gen = ZeroGeneration(3, 3)

        target = [1, 0]

        next_generation = NextGeneration(target, zero_gen.zero_generation)
        next_generation.create_next_generation(10)

        self.assertEqual(next_generation.green_counter, 5)

    @unittest.mock.patch('builtins.input', side_effect=["1001", "1111", "0100", "1010", "1, 0, 10"])
    def test_example_two(self, mock):
        """[1]
        Should create next generations and
        count how many times was the target green"""
        zero_gen = ZeroGeneration(4, 4)

        target = [2, 2]

        next_generation = NextGeneration(target, zero_gen.zero_generation)
        next_generation.create_next_generation(15)

        self.assertEqual(next_generation.green_counter, 14)


if __name__ == '__main__':
    unittest.main()
