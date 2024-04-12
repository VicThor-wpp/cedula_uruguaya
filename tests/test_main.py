
import unittest
from cedula_uruguaya.main import CedulaUruguaya

class TestCedulaUruguaya(unittest.TestCase):

    def test_get_validation_digit(self):
        self.assertEqual(CedulaUruguaya.get_validation_digit(3298763), 4)
        self.assertEqual(CedulaUruguaya.get_validation_digit(1234567), 5)
        self.assertEqual(CedulaUruguaya.get_validation_digit(1111111), 3)

    def test_clean_ci(self):
        self.assertEqual(CedulaUruguaya.clean_ci('3.298.763-4'), 32987634)
        self.assertEqual(CedulaUruguaya.clean_ci('123.456-7'), 1234567)
        self.assertEqual(CedulaUruguaya.clean_ci('1.111.111-1'), 11111111)

    def test_validate_ci(self):
        self.assertTrue(CedulaUruguaya.validate_ci('3.298.763-4'))
        self.assertFalse(CedulaUruguaya.validate_ci('3.298.763-7'))

    def test_format_ci(self):
        self.assertEqual(CedulaUruguaya.format_ci(32987634), '3.298.763-4')
        self.assertEqual(CedulaUruguaya.format_ci(1234567), '0.123.456-7')

    def test_random_ci_in_range(self):
        ci = CedulaUruguaya.random_ci_in_range(1000000, 2000000)
        self.assertTrue(1000000 <= int(str(ci)[:-1]) <= 2000000)
        self.assertTrue(CedulaUruguaya.validate_ci(ci))

    def test_international_format(self):
        self.assertEqual(CedulaUruguaya.international_format(32987634), 'UY-3.298.763-4')

    def test_bulk_validate_ci(self):
        results = CedulaUruguaya.bulk_validate_ci(['3.298.763-4', '1.234.567-8'])
        self.assertEqual(results, {'32987634': True, '12345678': False})

if __name__ == '__main__':
    unittest.main()
