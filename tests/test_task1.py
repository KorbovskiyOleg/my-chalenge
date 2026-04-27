import unittest
import sys
import os

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from task1 import SimpleArray


class TestSimpleArray(unittest.TestCase):
    """Unit tests for the SimpleArray class with constraints:
    - 0 <= len(num) <= 1000
    - -100 <= num[i] <= 100
    """

    def setUp(self):
        """Set up test fixtures."""
        self.sa = SimpleArray()

    def test_sum_num_empty_list(self):
        """Test sum_num with empty list (minimum length: 0)."""
        result = self.sa.sum_num([])
        self.assertEqual(result, 0)

    def test_sum_num_single_zero(self):
        """Test sum_num with single zero value."""
        result = self.sa.sum_num([0])
        self.assertEqual(result, 0)

    def test_sum_num_single_positive(self):
        """Test sum_num with single positive value at boundary (100)."""
        result = self.sa.sum_num([100])
        self.assertEqual(result, 100)

    def test_sum_num_single_negative(self):
        """Test sum_num with single negative value at boundary (-100)."""
        result = self.sa.sum_num([-100])
        self.assertEqual(result, -100)

    def test_sum_num_multiple_values(self):
        """Test sum_num with multiple values within range."""
        result = self.sa.sum_num([1, 2, 3])
        self.assertEqual(result, 6)

    def test_sum_num_all_positive_boundary(self):
        """Test sum_num with all values at positive boundary (100)."""
        result = self.sa.sum_num([100, 100, 100])
        self.assertEqual(result, 300)

    def test_sum_num_all_negative_boundary(self):
        """Test sum_num with all values at negative boundary (-100)."""
        result = self.sa.sum_num([-100, -100, -100])
        self.assertEqual(result, -300)

    def test_sum_num_mixed_values(self):
        """Test sum_num with mixed positive and negative values."""
        result = self.sa.sum_num([50, -50, 25, -25])
        self.assertEqual(result, 0)

    def test_sum_num_large_array(self):
        """Test sum_num with large array (near max length: 1000 elements)."""
        large_array = [1] * 1000
        result = self.sa.sum_num(large_array)
        self.assertEqual(result, 1000)

    def test_sum_num_max_length_all_ones(self):
        """Test sum_num with maximum length array (1000 elements) of ones."""
        result = self.sa.sum_num([1] * 1000)
        self.assertEqual(result, 1000)

    def test_sum_num_max_length_all_neg_hundred(self):
        """Test sum_num with maximum length array (1000 elements) of -100."""
        result = self.sa.sum_num([-100] * 1000)
        self.assertEqual(result, -100000)

    def test_sum_num_max_length_all_pos_hundred(self):
        """Test sum_num with maximum length array (1000 elements) of 100."""
        result = self.sa.sum_num([100] * 1000)
        self.assertEqual(result, 100000)

    def test_sum_num_default_argument(self):
        """Test sum_num with default argument."""
        result = self.sa.sum_num()
        self.assertEqual(result, 3)

    def test_sum_num_boundary_values(self):
        """Test sum_num with boundary values (-100, 0, 100)."""
        result = self.sa.sum_num([-100, 0, 100])
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
