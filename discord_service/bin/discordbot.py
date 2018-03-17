#!/bin/python

from discord.client import Client
import tornado.web
from tornado.ioloop import IOLoop
from tornado.options import define, parse_command_line, options


class BotRequestHandler(tornado.web.RequestHandler):
    def initialize(self, bot=None):
        self.bot = bot


class UserHandler(BotRequestHandler):
    def delete(self, *args, **kwargs):
        # remove user from server
        pass

    def post(self, *args, **kwargs):
        # add user to server
        pass

    def patch(self, *args, **kwargs):
        # edit user (roles, nickname)
        pass

    def get(self, *args, **kwargs):
        # gets a list of users? idk
        pass


# These are the command line options. Anything without a default is required.
define('port', default=8888, help='port to listen on', type=int)
define('host', default='127.0.0.7', help='host address to bind to', type=str)
define('token', help='discord bot token', type=str)
# define('bot', help='dotted path to module containing custom bot "Class"', default='discord.client', type='str')


if __name__ == '__main__':
    # populates `options` with command line args
    parse_command_line()

    # creates and logs in the bot
    # bot = __import__(options.bot).Client()
    bot = Client()
    bot.start()
    bot.login(options.token)

    # creates the Tornado web app
    app = tornado.web.Application(
        (r'/users/([0-9]*)', UserHandler, dict(bot=bot))  # user ID in urls? or body?
    )
    app.listen(options.port, address=options.host)

    # begins the web app
    IOLoop.current().start()
