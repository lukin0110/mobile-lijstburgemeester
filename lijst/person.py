# -- coding: utf-8 --
__author__ = 'maarten'


class Person:
    def __init__(self, place, name, address, age, family, profession, career, leisure_time, interests, fun_fact, youtube, youtube_title, twitter, facebook, website):
        self.place = place
        self.name = name
        self.address = address
        self.age = age
        self.family = family
        self.profession = profession
        self.career = career
        self.leisure_time = leisure_time
        self.interests = interests
        self.fun_fact = fun_fact
        self.youtube = youtube
        self.youtube_title = youtube_title
        self.twitter = twitter
        self.facebook = facebook
        self.website = website

persons = {
# Plaats 1
'peter-vanvelthoven': Person(
    1,
    'Peter Vanvelthoven',
    'Kerkstraat 32A in Lommel CENTRUM',
    49,
    'gehuwd met Ingrid en twee kinderen:  Nathalie (18) en Sam (14)',
    'Burgemeester en volksvertegenwoordiger, Rechten gestudeerd',
    "Deputé van Limburg (1995),\n\
        Vlaams volksvertegenwoordiger (1995-1999),\n\
        Federaal volksvertegenwoordiger (1999-2003),\n\
        Staatssecretaris (2003-2005), minister (2005-2007),\n\
        Federaal volksvertegenwoordiger (2007),\n\
        en Burgemeester van Lommel sedert 2006",

    "Heeft vroeger veel gebasket en tennis gespeeld. Nu kijkt hij vooral naar het basketbal van de kinderen. "
    "Voor de rest af en toe een terrasje in Lommel. "
    "Kan genieten van een avond thuis met een goeie film'",

    'In heel veel dingen geïnteresseerd. Als burgemeester komt dat goed van pas',
    'Gek van Amerikaans basketbal',
    'http://www.youtube.com/watch?v=4VLmJ43fHpM&feature=results_main&playnext=1&list=PL11748D4EA7A9D1CE',
    None,
    None,
    None,
    'http://www.petervanvelthoven.be'
),

# Plaats 2
'an-vanden-boer': Person(
    2,
    'An Vander Boer',
    'Vreyshorring 15A in Lommel CENTRUM',
    26,
    'Vrijgezel',
    'Advocaat',
    "Nieuw",

    "An speelt tennis bij LTC waar ze ook bestuurslid is. "
    "Ze speelt basket bij K-Kontrol Lommel "
    "Houdt van films, lezen en kwissen bij quizploeg Bruudruuster.",

    'Sport, verkeer, onderwijs, welzijn',
    'Beide  grootvaders zaten ooit in de politiek',
    'http://www.youtube.com/watch?v=-ZJDNSp1QJA',
    'The piano - amazing short',
    None,
    None,
    'http://www.advoclommel.be'
),

#Plaats 3
'walter-cremers': Person(
    3,
    'Walter Cremers',
    'Peter Aertsstraat 10 in Lommel BARRIER',
    56,
    'Gehuwd met Christiane Poorters'
    'Vader van Jef, die getrouwd is met Heidi Geysmans en haar kinderen Annisce en Celince',
    'Landmeter / ambtenaar',

    "LOMMEL: 20 jaar Schepen, 1 jaar Wnd Burgemeester"
    "PROVINCIE: 18 jaar provincieraadslid en momenteel 3 jaar gedeputeerde ",

    "Wielertoerist en overtuigd ventourist, Wandelen",

    'Ruimtelijke Ordening, Sport, Dierenwelzijn, Mobiliteit',
    'Walter was 9 jaar lang de voorzitter van Interelectra',
    'http://www.youtube.com/watch?v=nfL8RGV-t2U&feature=related',
    "Fragment De Parelvissers",
    None,
    None,
    ''
),

#Plaats 4
'jasmine-vangrieken': Person(
    4,
    '',
    '',
    49,
    '',
    '',
    "",

    "",

    '',
    '',
    '',
    None,
    None,
    None,
    ''
),

#Plaats 5
'rita-phlippo': Person(
    5,
    '',
    '',
    49,
    '',
    '',
    "",

    "",

    '',
    '',
    '',
    None,
    None,
    None,
    ''
),

#Plaats 6
'johan-Hoeks': Person(
    6,
    '',
    '',
    49,
    '',
    '',
    "",

    "",

    '',
    '',
    '',
    None,
    None,
    None,
    ''
),

#Plaats 7
'loes-mispoelier': Person(
    7,
    '',
    '',
    49,
    '',
    '',
    "",

    "",

    '',
    '',
    '',
    None,
    None,
    None,
    ''
),

#Plaats 8,
'dominiek-van-eepoel': Person(
    8,
    '',
    '',
    49,
    '',
    '',
    "",

    "",

    '',
    '',
    '',
    None,
    None,
    None,
    ''
),

#Plaats 9
'mieke-berghmans': Person(
    9,
    '',
    '',
    49,
    '',
    '',
    "",

    "",

    '',
    '',
    '',
    None,
    None,
    None,
    ''
),

#Plaats 10
'esther-vreys': Person(
    10,
    '',
    '',
    49,
    '',
    '',
    "",

    "",

    '',
    '',
    '',
    None,
    None,
    None,
    ''
),

#Plaats 11
'atabey-yildiz': Person(
    11,
    '',
    '',
    49,
    '',
    '',
    "",

    "",

    '',
    '',
    '',
    None,
    None,
    None,
    ''
),

#Plaats 12
'martine-verboven': Person(
    12,
    '',
    '',
    49,
    '',
    '',
    "",

    "",

    '',
    '',
    '',
    None,
    None,
    None,
    ''
),

#Plaats 13
'chris-corens': Person(
    13,
    '',
    '',
    49,
    '',
    '',
    "",

    "",

    '',
    '',
    '',
    None,
    None,
    None,
    ''
),

#Plaats 14,
'freddy-bantje': Person(
    14,
    '',
    '',
    49,
    '',
    '',
    "",

    "",

    '',
    '',
    '',
    None,
    None,
    None,
    ''
),

#Plaats 15
'eefje-beckers': Person(
    15,
    '',
    '',
    49,
    '',
    '',
    "",

    "",

    '',
    '',
    '',
    None,
    None,
    None,
    ''
),

#Plaats 16,
'anick-berghmans': Person(
    16,
    '',
    '',
    49,
    '',
    '',
    "",

    "",

    '',
    '',
    '',
    None,
    None,
    None,
    ''
),

#Plaats 17
'kris-verduyckt': Person(
    17,
    '',
    '',
    49,
    '',
    '',
    "",

    "",

    '',
    '',
    '',
    None,
    None,
    None,
    ''
),

#Plaats 18
'liesbet-vanwelsenaers': Person(
    18,
    '',
    '',
    49,
    '',
    '',
    "",

    "",

    '',
    '',
    '',
    None,
    None,
    None,
    ''
),

#Plaats 19,
'rina-ven': Person(
    19,
    '',
    '',
    49,
    '',
    '',
    "",

    "",

    '',
    '',
    '',
    None,
    None,
    None,
    ''
),

#Plaats 20
'jean-kuyken': Person(
    20,
    '',
    '',
    49,
    '',
    '',
    "",

    "",

    '',
    '',
    '',
    None,
    None,
    None,
    ''
),

#Plaats 21
'jan-swinnen': Person(
    21,
    '',
    '',
    49,
    '',
    '',
    "",

    "",

    '',
    '',
    '',
    None,
    None,
    None,
    ''
),

#Plaats 22
'jean-lavreysen': Person(
    22,
    '',
    '',
    49,
    '',
    '',
    "",

    "",

    '',
    '',
    '',
    None,
    None,
    None,
    ''
),

#Plaats 23
'joke-loomans': Person(
    23,
    '',
    '',
    49,
    '',
    '',
    "",

    "",

    '',
    '',
    '',
    None,
    None,
    None,
    ''
),

#Plaats 24
'elly-vanbrabant': Person(
    24,
    '',
    '',
    49,
    '',
    '',
    "",

    "",

    '',
    '',
    '',
    None,
    None,
    None,
    ''
),

#Plaats 25
'erik-maes': Person(
    25,
    '',
    '',
    49,
    '',
    '',
    "",

    "",

    '',
    '',
    '',
    None,
    None,
    None,
    ''
),

#Plaats 26
'veerle-baert': Person(
    26,
    '',
    '',
    49,
    '',
    '',
    "",

    "",

    '',
    '',
    '',
    None,
    None,
    None,
    ''
),

#Plaats 27
'sally-de-jong': Person(
    27,
    '',
    '',
    49,
    '',
    '',
    "",

    "",

    '',
    '',
    '',
    None,
    None,
    None,
    ''
),

#Plaats 28
'ronny-geysen': Person(
    28,
    '',
    '',
    49,
    '',
    '',
    "",

    "",

    '',
    '',
    '',
    None,
    None,
    None,
    ''
),

#plaats 29
'danny-huijsmans': Person(
    29,
    '',
    '',
    49,
    '',
    '',
    "",

    "",

    '',
    '',
    '',
    None,
    None,
    None,
    ''
),

#Plaats 30,
'fons-haagdoren': Person(
    30,
    '',
    '',
    49,
    '',
    '',
    "",

    "",

    '',
    '',
    '',
    None,
    None,
    None,
    ''
),

#Plaats 31
'francois-timmermans': Person(
    31,
    '',
    '',
    49,
    '',
    '',
    "",

    "",

    '',
    '',
    '',
    None,
    None,
    None,
    ''
)}
