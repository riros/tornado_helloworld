from typing import Awaitable, Optional

from tornado.web import RequestHandler


class NumbersStoreHandler(RequestHandler):
    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

    def get(self):
        self.set_header("Content-Type", "text/plain")
        self.write("Hello, world")


class TestHandler(RequestHandler):
    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

    def get(self):
        self.set_header("Content-Type", "text/plain")
        self.write("Ok")
