from pyramid.config import Configurator

def main(global_config, **settings):
    """This function returns a Pyramid WSGI application."""
    with Configurator(settings=settings) as config:
        config.include('pyramid_debugtoolbar')
        config.add_static_view(name='static', path='tutorial:static')
        config.add_route('home', '/')
        config.scan()
        return config.make_wsgi_app()
