import unittest
import requests

class TestHolaMundo(unittest.TestCase):
    def test_homepage(self):
        response = requests.get('http://localhost')
        self.assertEqual(response.status_code, 200)
        self.assertIn('<h1>Hola Mundo</h1>', response.text)

if __name__ == '__main__':
    unittest.main()
