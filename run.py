import contextvars

from tornado.ioloop import IOLoop
from tornado.options import define, options
import tornado
from tornado.web import RequestHandler
from tortoise import Tortoise

from urls import router


define("port", default=8888, help="run on the given port", type=int)
define('debug', default=True, help='set tornado debug mode', type=bool)
define('DB_NAME', default='tornado', help='Tornado db name', type=str)
define('DB_HOST', default='localhost', help='db host name', type=str)
options.parse_command_line()

app = tornado.web.Application(
    router,
    debug=True,
)

testing_var = contextvars.ContextVar('testing')


async def run():
    await Tortoise.init(
        {
            "connections": {
                "default": {
                    "engine": "tortoise.backends.asyncpg",
                    "credentials": {
                        "host": "localhost",
                        "port": "5432",
                        "user": "postgres",
                        "password": "postgres",
                        "database": options.DB_NAME + '_test' if testing_var.get() else '',
                    },
                }
            },
            "apps": {"models": {"models": ["models"], "default_connection": "default"}},
        },
        # _create_db=True,
    )
    await Tortoise.generate_schemas()


def init_app(loop, test=False):
    if test:
        testing_var.set(True)
    loop.run_sync(run)
    return app


def main():
    loop = IOLoop.current()

    application = init_app(loop=loop)
    application.listen(options.port)
    loop.start()


if __name__ == "__main__":
    main()
