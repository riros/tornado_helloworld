from tornado.testing import AsyncHTTPTestCase

import run


class AnyTestCase(AsyncHTTPTestCase):
    def get_app(self):
        return run.init_app(self.io_loop, test=True)

    # def send_post(self, url, data):
    # return self.fetch(url, method='POST', body=json.dumps(data),
    #                   headers={'Content-Type': 'application/json'})

    @staticmethod
    def body_string(response):
        return response.body.decode('utf-8')

    # def test_http_fetch(self):
    #     """ проверка базовой функциональности работы сервера """
    #     response = self.fetch('/test')
    #     self.assertEqual(response.code, 200)
    #     self.assertEqual(response.body, b'Ok')

    def test_crud(self):
        """
        Проверка основной логики приложения
        :return:
        """
        test_text = 'test'

        # проверит начальные значения данных
        response = self.fetch('/read')
        self.assertEqual(response.body, b'')

        # обновление данных
        response = self.fetch('/write', method='POST', body=test_text)
        self.assertEqual(response.code, 200)
        self.assertEqual(self.body_string(response), test_text)

        # обнуление данных
        response = self.fetch('/reset', method='DELETE')
        self.assertEqual(response.code, 200)
        self.assertEqual(self.body_string(response), 'ok')
