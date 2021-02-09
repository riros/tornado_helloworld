import json

from tornado.testing import AsyncHTTPTestCase

from main import make_app


class NumbersTestCase(AsyncHTTPTestCase):
    def get_app(self):
        return make_app()

    def send_post(self, url, data):
        return self.fetch(url, method='POST', body=json.dumps(data),
                          headers={'Content-Type': 'application/json'})

    @staticmethod
    def body_string(response):
        return response.body.decode('utf-8')

    def test_http_fetch(self):
        response = self.fetch('/test')
        self.assertEqual(response.code, 200)
        self.assertEqual(response.body, b'Ok')

    def test_crud(self):
        """
        Проверка основной логики
        :return:
        """
        test_dict = {'data': 'ddd'}

        # test init
        response = self.fetch('/')
        self.assertEqual(response.body, b'{}')

        # test update
        response = self.send_post('/', test_dict)
        self.assertEqual(response.code, 200)
        self.assertEqual(self.body_string(response), json.dumps(test_dict))

        # test delete
        response = self.fetch('/', method='DELETE')
        self.assertEqual(response.code, 200)
        self.assertEqual(self.body_string(response), json.dumps({}))
