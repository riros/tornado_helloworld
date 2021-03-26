from typing import Awaitable, Optional

from tornado.web import RequestHandler

from models import Text


class WriteHandler(RequestHandler):
    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

    async def post(self):
        await Text.create(value=self.request.body)
        self.write(self.request.body)


class ResetHandler(RequestHandler):
    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

    def get(self):
        self.delete()

    async def delete(self):
        text = await Text.filter().first()
        ret = 'Not found'
        if text:
            await text.delete()
            ret = 'ok'

        self.write(ret)


class ReadHandler(RequestHandler):
    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

    async def get(self):
        text = await Text.filter(value=self.request.body).first()
        if text:
            self.write(text.id)
        else:
            self.write("")


class TestHandler(RequestHandler):
    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

    def get(self):
        self.set_header("Content-Type", "text/plain")
        self.write("Ok")
