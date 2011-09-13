from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import taskqueue
from google.appengine.ext import db
from google.appengine.ext.webapp import template
from django.utils import simplejson

import urllib,urllib2
import re

class MainApp(webapp.RequestHandler):
    
    def get(self) :
        
        sites = [
        'emol.com',
        'latercera.com',
        'cooperativa.cl',
        'nacion.cl',
        'elmostrador.cl',
        'terra.cl',
        ]
        
        for site in sites :
            # enc_site = urllib.urlencode(site)
            self.response.out.write("Querying for %s <br />" % site)
            request = "http://search.twitter.com/search.json?q=" + site + "&result_type=mixed&count=5"
            res = urllib2.urlopen(request)
            json = simplejson.loads(res.read())
            tweets = json['results']
            
            for tweet in tweets :
                #matches = re.search("\b(([\w-]+://?|www[.])[^\s()<>]+(?:\([\w\d]+\)|([^[:punct:]\s]|/)))", tweet)
                
                #for match in matches :
                #    self.response.out.write(match)
                    
                self.response.out.write(tweet['text'])
                self.response.out.write("<br /><be />")