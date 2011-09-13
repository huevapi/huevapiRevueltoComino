from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import taskqueue
from google.appengine.ext import db
from google.appengine.ext.webapp import template

class MainApp(webapp.RequestHandler):
    
    def get(self) :
        
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Hello, webapp World!')