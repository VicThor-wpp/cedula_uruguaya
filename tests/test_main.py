import unittest

from cedula_uruguaya import (
    bulk_validate_ci,
    clean_ci,
    format_ci,
    get_validation_digit,
    international_format,
    random_ci_in_range,
    validate_ci,
)


class TestCedulaUruguaya(unittest.TestCase):
    def test_get_validation_digit(self):
        # Using known valid values based on standard algorithm
        # Example from documented algorithms: 1.234.567 -> Check digit 2
        self.assertEqual(get_validation_digit(1234567), 2)

        # Recalculated for 3298763: Result is 6
        self.assertEqual(get_validation_digit(3298763), 6)

        # Test 1111111 -> 1*2+1*9+1*8+1*7+1*6+1*3+1*4 = 39. Remainder 9. Check 1.
        self.assertEqual(get_validation_digit(1111111), 1)

    def test_clean_ci(self):
        self.assertEqual(clean_ci("3.298.763-6"), 32987636)
        self.assertEqual(clean_ci("123.456-7"), 1234567)
        self.assertEqual(clean_ci("1.111.111-1"), 11111111)
        self.assertEqual(clean_ci(32987636), 32987636)

    def test_validate_ci(self):
        # Valid CIs
        self.assertTrue(validate_ci("3.298.763-6"))
        self.assertTrue(validate_ci(32987636))
        self.assertTrue(validate_ci("1.234.567-2"))

        # Invalid CIs
        self.assertFalse(validate_ci("3.298.763-4"))  # Wrong digit
        self.assertFalse(validate_ci(12345678))  # Wrong digit (should be 2)

    def test_format_ci(self):
        # 3.298.763-6
        self.assertEqual(format_ci(32987636), "3.298.763-6")
        # 1.234.567-2 -> 1.234.567-2
        self.assertEqual(format_ci(12345672), "1.234.567-2")
        # Short CI: 123456 (valid check digit?)
        # 12.345-X
        self.assertEqual(format_ci(123456), "12.345-6")

    def test_random_ci_in_range(self):
        ci = random_ci_in_range(1000000, 2000000)
        self.assertTrue(1000000 <= int(str(ci)[:-1]) <= 2000000)
        self.assertTrue(validate_ci(ci))

    def test_international_format(self):
        self.assertEqual(international_format(32987636), "UY-3.298.763-6")

    def test_bulk_validate_ci(self):
        # Using a valid and an invalid CI
        # 3.298.763-6 is Valid
        # 1.234.567-8 is Invalid (should be -2)
        results = bulk_validate_ci(["3.298.763-6", "1.234.567-8"])
        self.assertEqual(results, {"3.298.763-6": True, "1.234.567-8": False})


if __name__ == "__main__":
    unittest.main()
