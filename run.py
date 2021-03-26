from tornado.ioloop import IOLoop
from tornado.options import define, options

from application import app


define("port", default=8888, help="run on the given port", type=int)


def make_app():
    return app


def main():
    options.parse_command_line()
    application = make_app()
    application.listen(options.port)
    loop = IOLoop.current().start()


if __name__ == "__main__":
    main()
