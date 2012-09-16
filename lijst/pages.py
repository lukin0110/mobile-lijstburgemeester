# Welcome to some quick and dirty hacks and copy paste code
import random
import string
from django.template import TemplateDoesNotExist


import logging
from datetime import datetime, date, timedelta
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext import db
from person import persons
from person import persons_sorted
from operator import itemgetter
from operator import attrgetter

class IndexPage(webapp.RequestHandler):
    def get(self):
        values = {'menu': 'logo'}
        self.response.out.write(template.render('templates/index.html',values))


class PersonPage(webapp.RequestHandler):
    def get(self, path):
        values = {
            'path': path,
            'history': '/',
            'spam': 'eggs',
            'persons': persons_sorted,
            'persons2': persons
        }

        if len(path) == 0:
            values["menu"] = "back"
            self.response.out.write(template.render('templates/persons.html',values))
        else:
            person = persons[string.replace(path, "/", "")]
            values["menu"] = "persons"
            values["person"] = person

            if person.place == 31:
                values["next"] = "/wie/"
            else:
                values["next"] = persons_sorted[person.place][0]

            if person.place == 1:
                values["previous"] = "/wie/"
            else:
                values["previous"] = persons_sorted[person.place-2][0]

            self.response.out.write(template.render('templates/person.html',values))


class CatchallPage(webapp.RequestHandler):
    def get(self):
        try:
            path = self.request.path
            values = {'menu':'back'}

            if path == "/" or path is None:
                path = "/index"
                values['menu'] = 'logo'

            str = "templates" + path + ".html"
            self.response.out.write(template.render(str,values))
        except TemplateDoesNotExist:
            self.response.set_status(404)
            self.response.out.write(template.render('templates/404.html', {}))


class GamePage(webapp.RequestHandler):
    def get(self, path):
        chosenOne = self.getRandom()
        values = {
            'menu':'back',
            'person': chosenOne,
            'step':1,
            'answers': self.getAnswers(chosenOne)
        }
        self.response.out.write(template.render("templates/spelStap.html",values))

    def getAnswers(self, chosenOne):
        answers = [
            chosenOne,
            self.getRandom(),
            self.getRandom()
        ]
        # everyday i'm shuffling
        random.shuffle(answers)
        return answers

    def getRandom(self):
        index = random.randint(1, 31)
        person = persons_sorted[index-1][1]

        while not person.pic_youth:
            index = random.randint(1, 31)
            person = persons_sorted[index-1][1]

        return person






