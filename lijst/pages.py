# Welcome to some quick and dirty hacks and copy paste code
from django.template import TemplateDoesNotExist


import logging
from datetime import datetime, date, timedelta
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext import db
from person import persons
from operator import itemgetter
from operator import attrgetter

class IndexPage(webapp.RequestHandler):
    def get(self):
        values = {'game': True, 'noBack': True}
        self.response.out.write(template.render('templates/index.html',values))


class PersonPage(webapp.RequestHandler):
    def get(self, path):

        #sorted(d.items(), key=itemgetter(1))
        #input.sort(lambda x,y : cmp(x['name'], y['name']))
        #sorted_persons = sorted(persons.items(), key=itemgetter(0))
        persons_sorted = sorted(persons.items(), key=lambda (k, v): float(v.place))

        values = {
            'path': path,
            'spam': 'eggs',
            'persons': persons_sorted,
            'persons2': persons
        }

        if len(path) == 0:
            self.response.out.write(template.render('templates/persons.html',values))
        else:
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


