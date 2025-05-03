import app
import unittest

class TestValidate(unittest.TestCase):
    def test_get_location(self):
        self.assertIsNotNone(app.get_location(17701))
        self.assertIsNotNone(app.get_location("53535"))
        self.assertEqual(app.get_location(758493), (None, None))
        self.assertEqual(app.get_location("sdf78"), (None, None))

    def test_get_weather(self):
        self.assertIsNotNone(app.get_weather(17701))
        self.assertIsNotNone(app.get_weather("53535"))
        self.assertEqual(app.get_weather(758493), (None, None))
        self.assertEqual(app.get_weather("sdf78"), (None, None))

if __name__ == '__main__':
    unittest.main()