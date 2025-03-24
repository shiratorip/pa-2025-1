import unittest
from unittest import mock
from round0.round_0_problem_1 import solve

class TestRoundTask1(unittest.TestCase):
    @mock.patch('builtins.input', create=True)
    def test_0_1(self, mocked_input):
        # Split input into separate lines to mock multiple input calls
        mocked_input.side_effect = [
            "7 8 9",
            "1 5 7",
            "2 2 3",
            "3 8",
            "2 10 8",
            "3 3",
            "1 12 12",
            "2 10 13",
            "1 9 14",
            "2 4",
            "5 7",
            "11 5",
            "15 1",
            "15 2",
            "15 3",
            "15 4",
            "15 5",
            "15 6"
        ]
        result = solve()
        expected = "TAK\nNIE\nNIE\nTAK\nTAK\nNIE\nTAK\nNIE\nTAK"
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()