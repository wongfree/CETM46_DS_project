#!/usr/bin/env python
#
# Runs a Tornado web server with a django project
# Make sure to edit the DJANGO_SETTINGS_MODULE to point to your settings.py
#
# http://localhost:8080/hello-tornado
# http://localhost:8080

import sys, os, socket,uuid,subprocess,platform,re, json
from tornado.options import options, define, parse_command_line
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.wsgi
from django.core.wsgi import get_wsgi_application

define('port', type=int, default=80)


class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello from tornado')

def mycallback():
    pass

def main():
    os.environ['DJANGO_SETTINGS_MODULE'] = 'web.settings'

    settings = {
    "static_path": os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'freechatbot','static'),
    "static_url_prefix": "/static/"
    #"xsrf_cookies": True,
	#"debug":True,
            }
    parse_command_line()

    wsgi_app = get_wsgi_application()
    container = tornado.wsgi.WSGIContainer(wsgi_app)
    STATIC_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
    MEDIA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'media')


    tornado_app = tornado.web.Application(
        [
			(r'/static/(.*)', tornado.web.StaticFileHandler, {'path': STATIC_PATH}), 
			(r'/media/(.*)', tornado.web.StaticFileHandler, {'path': MEDIA_PATH}),
            ('.*', tornado.web.FallbackHandler, dict(fallback=container)),
            #dict(path=settings['static_path','media_path']),
			
        ],debug=True)
    server = tornado.httpserver.HTTPServer(tornado_app)
    server.listen(options.port)
    
    ioloop = tornado.ioloop.IOLoop.instance()

    # background update every x seconds
    task = tornado.ioloop.PeriodicCallback(
            mycallback,
            1000*60)
    task.start()

    ioloop.start()

if __name__ == '__main__':
    main()
