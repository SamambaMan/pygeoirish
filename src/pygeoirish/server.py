import logging
import os

from .routes import setup_routes
from aiohttp import web


async def init():
    app = web.Application()
    setup_routes(app)

    return app


def serve():
    logging.basicConfig(level=logging.DEBUG)

    port = int(os.environ.get("PORT", 8080))
    app = init()
    web.run_app(app, port=port)
