import os.path
import tornado.ioloop
import tornado.web

from tornado.options import define, options
from routers import urlpatterns

define("debug", default=True, help="run in debug mode", type=bool)
define("port", default=8000, help="run on the given port", type=int)


class Application(tornado.web.Application):

    def __init__(self):
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=True,
        )
        tornado.web.Application.__init__(self, urlpatterns, **settings)


def main():
    tornado.options.parse_command_line()
    print("Starting server at http://0.0.0.0:%s/") % options.port
    app = Application()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
