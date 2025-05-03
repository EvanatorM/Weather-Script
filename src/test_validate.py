import validate
import unittest
import config as config
import requests
import json

class TestValidate(unittest.TestCase):
    def test_validate_zip(self):
        self.assertTrue(validate.validate_zip("43295"))
        self.assertTrue(validate.validate_zip("12478"))
        self.assertFalse(validate.validate_zip("124784"))
        self.assertFalse(validate.validate_zip("1247"))
        self.assertFalse(validate.validate_zip("12478-3829"))
        self.assertFalse(validate.validate_zip("ew9883"))
        self.assertFalse(validate.validate_zip("1983e"))
        self.assertFalse(validate.validate_zip(34234))
        self.assertFalse(validate.validate_zip(3424))

    def test_validate_address(self):
        res = requests.get(f"https://maps.googleapis.com/maps/api/geocode/json?address=17701&key={config.GEOCODE_API_KEY}")
        self.assertTrue(validate.validate_address(json.loads(res.content)))
        self.assertFalse(validate.validate_address({"asdf": 53}))
        self.assertFalse(validate.validate_address(432))
        self.assertFalse(validate.validate_address("apsidhf"))

    def test_validate_lat_long(self):
        self.assertTrue(validate.validate_lat_long(12.57, 75.32))
        self.assertTrue(validate.validate_lat_long("73.53", "21.5324"))
        self.assertFalse(validate.validate_lat_long("-94.03", "53.923"))
        self.assertFalse(validate.validate_lat_long("109.03", "43.25"))
        self.assertFalse(validate.validate_lat_long("23.59", "-185.32"))
        self.assertFalse(validate.validate_lat_long("23.59", "195.32"))
        self.assertFalse(validate.validate_lat_long("asef", "23fd"))
        self.assertFalse(validate.validate_lat_long("93f", "23f"))

    def test_validate_weather(self):
        res = requests.get(f"https://api.tomorrow.io/v4/weather/forecast?location=17.25,18.34&apikey={config.TOMORROW_API_KEY}&units=imperial")
        self.assertTrue(validate.validate_weather(res.content))
        self.assertFalse(validate.validate_address({"asdf": 53}))
        self.assertFalse(validate.validate_address(432))
        self.assertFalse(validate.validate_address("apsidhf"))

if __name__ == '__main__':
    unittest.main()