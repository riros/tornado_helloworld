import tornado
from tornado import ioloop
from tornado.options import define, options
from tornado.web import RequestHandler

from views import NumbersStoreHandler, TestHandler


define("port", default=8888, help="run on the given port", type=int)


def make_app():
    return tornado.web.Application([
        (r"/", NumbersStoreHandler),
        (r"/test", TestHandler),

    ])


def main():
    options.parse_command_line()
    app = make_app()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
