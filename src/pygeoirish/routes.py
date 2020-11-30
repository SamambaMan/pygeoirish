from .views import geocode_address


def setup_routes(app):
    router = app.router
    router.add_get(
        '/geocode/{query}', geocode_address, name='geocode'
    )
