import unittest
import app.app as app

class TestApp(unittest.TestCase):
    def test_when_is_x_1600(self):
        self.assertEqual(app.is_leap_year(1600), 'True')
    def test_when_is_x_2000(self):
        self.assertEqual(app.is_leap_year(2001), 'False')
    def test_when_is_x_2400(self):
        self.assertEqual(app.is_leap_year(2400), 'True')

if __name__ == '__main__':
    unittest.main()