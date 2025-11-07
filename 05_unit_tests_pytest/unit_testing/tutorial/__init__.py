from pyramid.config import Configurator
from pyramid.response import Response

def hello_world(request):
    return Response('<body><h1>Hello World!</h1></body>')

def main(global_config, **settings):
    """This function returns a Pyramid WSGI application."""
    with Configurator(settings=settings) as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        return
