import logging

from .routes import setup_routes
from aiohttp import web


async def init():
    app = web.Application()
    setup_routes(app)

    return app


def serve():
    logging.basicConfig(level=logging.DEBUG)

    app = init()
    web.run_app(app)
