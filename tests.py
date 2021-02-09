from tornado.testing import AsyncHTTPTestCase

from main import make_app


class NumbersTestCase(AsyncHTTPTestCase):
    def get_app(self):
        return make_app()

    def test_http_fetch(self):
        response = self.fetch('/test')
        self.assertEqual(response.code, 200)
        self.assertEqual(response.body, b'Ok')
