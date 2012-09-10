from django.template import TemplateDoesNotExist

__author__ = 'maarten'
# Welcome to some quick and dirty hacks and copy paste code

import logging
from datetime import datetime, date, timedelta
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext import db

class IndexPage(webapp.RequestHandler):
    def get(self):
        values = {}
        self.response.out.write(template.render('templates/index.html',values))


class PersonPage(webapp.RequestHandler):
    def get(self, path):

        values = {
            'path': path,
            'spam': 'test'
        }

        self.response.out.write(template.render('templates/person.html',values))


class CatchallPage(webapp.RequestHandler):
    def get(self):
        try:
            path = self.request.path
            str = "templates" + path + ".html"
            values = {}
            self.response.out.write(template.render(str,values))
        except TemplateDoesNotExist:
            self.response.set_status(404)
            self.response.out.write(template.render('templates/404.html', {}))


