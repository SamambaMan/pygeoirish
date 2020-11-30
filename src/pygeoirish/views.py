from aiohttp import web
from .geocoder import geocode


async def geocode_address(request):
    query = request.match_info.get('query')
    response = geocode(query)
    return web.json_response(response)
