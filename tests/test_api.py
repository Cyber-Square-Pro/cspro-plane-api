from django.test import SimpleTestCase

from api.utils import is_sum_even


class UtilityTests(SimpleTestCase):
    def test_sum_is_even(self):
        """Test cases where the sum should be even."""
        # 2 + 2 = 4 (Even)
        assert is_sum_even(2, 2) is True

        # -1 + 1 = 0 (Even)
        assert is_sum_even(-1, 1) is True

    def test_sum_is_odd(self):
        """Test cases where the sum should be odd."""
        # 2 + 3 = 5 (Odd)
        assert is_sum_even(2, 3) is False

        # 0 + 7 = 7 (Odd)
        assert is_sum_even(0, 7) is False

    def test_logic_with_assertEqual(self):
        """Using Django's built-in assertion for better error messages."""
        result = is_sum_even(10, 10)
        self.assertEqual(result, True, "Sum of 10 and 10 should be even")
