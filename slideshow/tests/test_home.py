from django.test import TestCase

class TestHome(TestCase):
    def test_home_ok(self):
        response = self.client.get('/')
        self.assertEqual(200, response.status_code)
