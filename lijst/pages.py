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
                values["next"] = "/wie/" + persons_sorted[person.place][0]

            if person.place == 1:
                values["previous"] = "/wie/"
            else:
                values["previous"] ="/wie/" + persons_sorted[person.place - 2][0]

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
        step = self.parseInt(path.replace("/", ""), -1)

        if 0 < step < 11:
            self.doGame(step)
        else:
            self.doFinish()

    def doGame(self, step):
        state = base64.urlsafe_b64decode(str(self.request.get("d"))).split(",")

        if len(state) > 1:
            param_score = self.parseInt(state[1], 0)
        else:
            param_score = 0

        self.possibleValues = range(1, 32)
        param_done = str(state[0]).split("|")
        param_correct = base64.urlsafe_b64decode(str(self.request.get("c")))
        param_choice = self.parseInt(self.request.get("q"), -1)
        logger.info("Correct = " + param_correct)

        # http://wiki.python.org/moin/KeyError
        #person_correct = persons[param_correct]
        person_correct = persons.get(param_correct, None)
        result = None

        # Check the result
        if person_correct is not None and person_correct.place == param_choice:
            result = "success"
            param_score += 1
        elif param_choice != -1:
            result = "error"

        # Remove
        for place in param_done:
            self.remove(place)

        chosenOne = self.getRandom()

        self.remove(chosenOne[1].place)
        param_done.append(chosenOne[1].place)

        values = {
            'page': PageMeta("Het Lijst Burgemeester spel", "Kwis, fotos, kandidaten, mobile", "De foto kwis"),
            'menu': 'spel',
            'person': chosenOne[1],
            'personCorrect': person_correct,
            'correct': base64.urlsafe_b64encode(chosenOne[0]),
            'done': base64.urlsafe_b64encode("|".join(str(x) for x in param_done) + "," + str(param_score)),
            'step': step,
            'answers': self.getAnswers(chosenOne),
            'result': result,
            'score': param_score,
            'debug':"|".join(str(x) for x in self.possibleValues)
                    + ", " + "|".join(str(x) for x in param_done)
                    + ", " + str(param_score)
        }
        self.response.out.write(template.render("templates/spelStap.html", values))

    def doFinish(self):
        state = base64.urlsafe_b64decode(str(self.request.get("d"))).split(",")
        if len(state) > 1:
            param_score = self.parseInt(state[1], 0)
        else:
            param_score = 0

        if param_score > 5:
            cheer = "Hoera"
        elif param_score == 5:
            cheer = "Hmmm"
        else:
            cheer = "Oops"

        values = {
            'menu': 'spel',
            'cheer': cheer,
            'score': param_score,
        }
        self.response.out.write(template.render("templates/spelEinde.html", values))

    def getAnswers(self, chosenOne):
        answers = [
            chosenOne[1],
            self.getRandom(chosenOne[1].gender)[1],
            self.getRandom(chosenOne[1].gender)[1]
        ]
        # everyday i'm shuffling
        random.shuffle(answers)
        return answers

    def getRandom(self, gender=None):
        """
        Returns a random person, with some excludes in mind.  The returned value is a tuple (key, value)
        """
        logger.info("Gender = " + str(gender))
        #index = random.randint(1, 31)
        index = random.choice(self.possibleValues)
        #persons_sorted is zero based
        person = persons_sorted[index - 1]
        found = False

        #while not person[1].pic_youth:
        while not found:
            index = random.choice(self.possibleValues)
            person = persons_sorted[index - 1]

            if person[1].pic_youth:
                if gender is not None and gender != person[1].gender:
                    found = False
                else:
                    found = True
                    self.remove(person[1].place)
        return person

    def remove(self, value):
        try:
            self.possibleValues.remove(int(value))
        except ValueError:
            pass

    def parseInt(self, str, defaultValue):
        try:
            return int(str)
        except ValueError:
            return defaultValue









