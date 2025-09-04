import unittest
from unittest.mock import Mock, patch
import requests

def get_weather(city):
    response=requests.get(f"https://www.timeanddate.com/weather/india/{city}")
    return response

class TestWeather_api(unittest.TestCase):
    @patch('requests.get')
    def test_get_weather(self, mock_get):
        #mock code
        mock_get.return_value.json.return_value = {'temp': 28}
        #testing with mock
        result=get_weather("Mumbai")
        print(result)
        self.assertEqual(result['temp'],28)
        
if __name__ == "__main__":
    unittest.main()