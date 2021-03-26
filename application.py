import tornado
from tornado.web import RequestHandler

from views import ReadHandler, ResetHandler, TestHandler, WriteHandler


app = tornado.web.Application([
    (r"/read", ReadHandler),
    (r'/write', WriteHandler),
    (r'/reset', ResetHandler),

    (r"/test", TestHandler),

])
