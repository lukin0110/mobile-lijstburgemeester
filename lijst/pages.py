# Welcome to some quick and dirty hacks and copy paste code
import base64
import random
import string
import urllib
from django.template import TemplateDoesNotExist

import logging
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from person import persons
from person import persons_sorted

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
            values["preload"] = "poster"
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
                'page': PageMeta("Speel het Lijst Burgemeester spel op je iPhone of Android, raad de jeugdfoto's van onze kandidaten ...", "Lommel, sp.a, kwis, lijst burgemeester, peter vanvelthoven, iphone, android, mobile", "Foto kwis")
            }

            if path == "/" or path is None:
                path = "/index"
                values['menu'] = 'logo'
            elif path == "/spel":
                values['preload'] = "youth"

            str = "templates" + path + ".html"
            self.response.out.write(template.render(str, values))
        except TemplateDoesNotExist:
            self.response.set_status(404)
            self.response.out.write(template.render('templates/404.html', {}))


class GamePage(webapp.RequestHandler):
    def get(self, path):
        self.step = self.parseInt(path.replace("/", ""), -1)
        self.state = base64.urlsafe_b64decode(str(self.request.get("d"))).split(",")
        self.param_done = str(self.state[0]).split("|")
        self.param_correct = base64.urlsafe_b64decode(str(self.request.get("c")))
        self.param_choice = self.parseInt(self.request.get("q"), -1)

        if len(self.state) > 1:
            self.param_score = self.parseInt(self.state[1], 0)
        else:
            self.param_score = 0

        # http://wiki.python.org/moin/KeyError
        #person_correct = persons[param_correct]
        self.person_correct = persons.get(self.param_correct, None)
        self.result = None

        # Check the result
        if self.person_correct is not None and self.person_correct.place == self.param_choice:
            self.result = "success"
            self.param_score += 1
        elif self.param_choice != -1:
            self.result = "error"

        # Redirect the page
        if 0 < self.step < 11:
            self.doGame()
        else:
            self.doFinish()

    def doGame(self):
        self.possibleValues = range(1, 32)
        logger.info("Correct = " + self.param_correct)

        # Remove
        for place in self.param_done:
            self.remove(place)

        chosenOne = self.getRandom()

        self.remove(chosenOne[1].place)
        self.param_done.append(chosenOne[1].place)

        values = {
            'page': PageMeta("Het Lijst Burgemeester spel", "Kwis, fotos, kandidaten, mobile", "De foto kwis"),
            'menu': 'spel',
            'person': chosenOne[1],
            'personCorrect': self.person_correct,
            'correct': base64.urlsafe_b64encode(chosenOne[0]),
            'done': base64.urlsafe_b64encode("|".join(str(x) for x in self.param_done) + "," + str(self.param_score)),
            'step': self.step,
            'answers': self.getAnswers(chosenOne),
            'result': self.result,
            'score': self.param_score,
            'debug':"|".join(str(x) for x in self.possibleValues)
                    + ", " + "|".join(str(x) for x in self.param_done)
                    + ", " + str(self.param_score)
        }
        self.response.out.write(template.render("templates/spelStap.html", values))

    def doFinish(self):
        if self.param_score > 5:
            cheer = "Hoera"
        elif self.param_score == 5:
            cheer = "Hmmm"
        else:
            cheer = "Oops"

        values = {
            'menu': 'spel',
            'cheer': cheer,
            'score': self.param_score,
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









