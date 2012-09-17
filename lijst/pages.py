# Welcome to some quick and dirty hacks and copy paste code
import base64
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

logger = logging.getLogger("pages")

class PageMeta:
    def __init__(self, desc, keywords, title):
        self.desc = desc
        self.keywords = keywords
        self.title = title


class IndexPage(webapp.RequestHandler):
    def get(self):
        values = {'menu': 'logo'}
        self.response.out.write(template.render('templates/index.html', values))


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
            values["page"] = PageMeta("Ontdek onze kandidaten", "Lommel, sp.a, kandidaten, lijst burgemeester", "Wie")
            self.response.out.write(template.render('templates/persons.html', values))
        else:
            person = persons[string.replace(path, "/", "")]
            values["menu"] = "persons"
            values["person"] = person
            values["page"] = PageMeta("Kandidaat: " + person.name, "Lommel, sp.a, kandidaten, lijst burgemeester, " + person.name, person.name)

            if person.place == 31:
                values["next"] = "/wie/"
            else:
                values["next"] = persons_sorted[person.place][0]

            if person.place == 1:
                values["previous"] = "/wie/"
            else:
                values["previous"] = persons_sorted[person.place - 2][0]

            self.response.out.write(template.render('templates/person.html', values))


class CatchallPage(webapp.RequestHandler):
    def get(self):
        try:
            path = self.request.path
            values = {
                'menu': 'back',
                #'page': PageMeta("Samen voor Lommel.  Lijst Burgemeester 2012", "Lommel, sp.a, lijst burgemeester, peter vanvelthoven, iphone, android, mobile", None)
                'page': PageMeta("Speel het Lijst Burgemeester spel, raad de jeugdfoto's van onze kandidaten ...", "Lommel, sp.a, kwis, lijst burgemeester, peter vanvelthoven, iphone, android, mobile", "Foto kwis")
            }

            if path == "/" or path is None:
                path = "/index"
                values['menu'] = 'logo'

            str = "templates" + path + ".html"
            self.response.out.write(template.render(str, values))
        except TemplateDoesNotExist:
            self.response.set_status(404)
            self.response.out.write(template.render('templates/404.html', {}))


class GamePage(webapp.RequestHandler):
    def get(self, path):
        self.possibleValues = range(1, 32)
        param_done = base64.urlsafe_b64decode(str(self.request.get("d"))).split("|")
        param_correct = base64.urlsafe_b64decode(str(self.request.get("c")))
        logger.info("Correct = " + param_correct)

        # Remove
        for place in param_done:
            self.remove(place)

        chosenOne = self.getRandom()

        self.remove(chosenOne[1].place)
        param_done.append(chosenOne[1].place)

        values = {
            'page': PageMeta("Het Lijst Burgemeester spel", "Kwis, fotos, kandidaten, mobile", "De foto kwis"),
            'menu': 'back',
            'person': chosenOne[1],
            'correct': base64.urlsafe_b64encode(chosenOne[0]),
            'done': base64.urlsafe_b64encode("|".join(str(x) for x in param_done)),
            'step': 1,
            'answers': self.getAnswers(chosenOne),
            'debug':"|".join(str(x) for x in self.possibleValues) + ", " + "|".join(str(x) for x in param_done)
        }
        self.response.out.write(template.render("templates/spelStap.html", values))

    def getAnswers(self, chosenOne):
        answers = [
            chosenOne[1],
            self.getRandom()[1],
            self.getRandom()[1]
        ]
        # everyday i'm shuffling
        random.shuffle(answers)
        return answers

    def getRandom(self):
        """
        Returns a random person, with some excludes in mind.  The returned value is a tuple (key, value)
        """
        #index = random.randint(1, 31)
        index = random.choice(self.possibleValues)
        #persons_sorted is zero based
        person = persons_sorted[index - 1]

        while not person[1].pic_youth:
            index = random.choice(self.possibleValues)
            person = persons_sorted[index - 1]
            self.remove(person[1].place)

        return person

    def remove(self, value):
        try:
            self.possibleValues.remove(int(value))
        except ValueError:
            pass







