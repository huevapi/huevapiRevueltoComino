from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import taskqueue
from google.appengine.ext import db
from google.appengine.ext.webapp import template
from django.utils import simplejson

import urllib,urllib2

class MainApp(webapp.RequestHandler):
    
    def get(self) :
        
        request = "http://search.twitter.com/search.json?q=cjmartin&result_type=mixed&count=5"
        res = urllib2.urlopen(request)
        json = simplejson.loads(res.read())
        
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write(json)