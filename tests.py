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
        """ проверка базовой функциональности работы сервера """
        response = self.fetch('/test')
        self.assertEqual(response.code, 200)
        self.assertEqual(response.body, b'Ok')

    def test_crud(self):
        """
        Проверка основной логики приложения
        :return:
        """
        test_dict = {'data': 'ddd'}

        # проверит начальные значения данных
        response = self.fetch('/')
        self.assertEqual(response.body, b'{}')

        # обновление данных
        response = self.send_post('/', test_dict)
        self.assertEqual(response.code, 200)
        self.assertEqual(self.body_string(response), json.dumps(test_dict))

        # обнуление данных
        response = self.fetch('/', method='DELETE')
        self.assertEqual(response.code, 200)
        self.assertEqual(self.body_string(response), json.dumps({}))
