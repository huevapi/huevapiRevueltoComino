#!/usr/bin/env python

import wsgiref.handlers
from google.appengine.ext import webapp

import NewsMashup

if __name__ == '__main__':

  handlers = [
    ('/', NewsMashup.MainApp),
    ]

  application = webapp.WSGIApplication(handlers, debug=True)
  wsgiref.handlers.CGIHandler().run(application)
