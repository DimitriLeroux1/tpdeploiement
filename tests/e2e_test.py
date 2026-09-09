import unittest
import requests


BASE_URL = "http://localhost:8080"


class TestE2E(unittest.TestCase):

    def test_health(self):
        response = requests.get(f"{BASE_URL}/health", timeout=5)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})

    def test_home(self):
        response = requests.get(f"{BASE_URL}/", timeout=5)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "<p>Hello, World!</p>")


if __name__ == "__main__":
    unittest.main()