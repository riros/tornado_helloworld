import json
from typing import Awaitable, Optional

from tornado.web import RequestHandler


data = {}


class WriteHandler(RequestHandler):
    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

    def post(self):
        global data
        data = json.loads(self.request.body)
        self.write(data)


class ResetHandler(RequestHandler):
    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

    def get(self):
        self.delete()

    def delete(self):
        global data
        data = {}
        self.set_header("Content-Type", "application/json")
        self.write(json.dumps(data))


class ReadHandler(RequestHandler):
    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

    def get(self):
        self.set_header("Content-Type", "application/json")
        self.write(json.dumps(data))


class TestHandler(RequestHandler):
    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

    def get(self):
        self.set_header("Content-Type", "text/plain")
        self.write("Ok")
