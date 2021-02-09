import tornado
from tornado.web import RequestHandler

from views import NumbersStoreHandler, TestHandler


app = tornado.web.Application([
    (r"/", NumbersStoreHandler),
    (r"/test", TestHandler),
])
