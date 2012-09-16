# -- coding: utf-8 --

class Person:
    def __init__(self, place, name, address, age, family, profession, career,
                 leisure_time, interests, fun_fact, youtube, youtube_title, twitter, facebook, website,
                 pic_youth):
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
        self.pic_youth = pic_youth

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
    'http://www.petervanvelthoven.be',
    True,
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
    'http://www.advoclommel.be',
    True,
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
    None,
    True,
),

#Plaats 4
'jasmine-vangrieken': Person(
    4,
    'Jasmine Vangrieken',
    'Weidestraat 45 in LUTLOMMEL',
    28,
    'Samenwonend met vriend Johan Vansummeren. ',
    'Orthopedagoge',
    "6 jaar Gemeenteraadslid",

    "Wielrennen, zwemmen, lopen."
    "Ik ga graag naar alle sporten kijken."
    "Filmpje mee pikken, terrasje doen."
    "Lekker uit eten gaan.",

    'Jeugd, sport, sociale zaken en welzijn',
    'Jasmine deed zelf jaren aan topsport (zwemmen) en trouwt in oktober',
    'http://www.youtube.com/watch?v=Q3Nsn-reFSc',
    "Laatste kilometer Johan Vansummeren",
    "@minavangrieken",
    None,
    None,
    True,
),

#Plaats 5
'rita-phlippo': Person(
    5,
    'Rita Phlippo',
    'Kerkhovensesteenweg 453 in Kerkhoven',
    46,
    'Gescheiden en 2 kinderen Nick (18) en Chloé (15)',
    'Apothekeres',
    "6 jaar gemeenteraadslid en zetelt in het bestuurscomité van Infrax",

    "Mensen bewust maken over hun gezondheid via preventie."
    "Salsadansen bij Salsa2You in Lommel."
    "Reizen, contact met andere culturen."
    "Fietsen en up to date blijven met mijn pubers.",

    'Sociale Zaken, welzijn en gezondheid, middenstand',
    'Rita organiseert al enkele jaren met veel succes gezondheidsavonden in het raadhuis.',
    'http://www.youtube.com/watch?v=Vk7eoKNrK8M',
    "The World Book of Happiness",
    None,
    "https://www.facebook.com/rita.phlippo",
    'http://www.apotheekphlippo.be',
    True,
),

#Plaats 6
'johan-hoeks': Person(
    6,
    'Johan Hoeks',
    'Rijkschoolstraat, CENTRUM',
    53,
    'Gehuwd met Vera Berben, vader van Maarten en "pake" van Xander en Elias',
    'Bedrijfsleider van Hoeks Verhuizingen en Kuismasters.com',
    "Nieuw",

    "Bestuurslid van service club '51 t' Zand' "
    "Hoofdsponsor van de Lommelse triatlon en gepassioneerd door deze sport Golfen",

    'Lokale economie, Veiligheid, Sport, Middenstand',
    '',
    'http://www.youtube.com/watch?v=Aank3dbGZ44',
    "Hoeks Triatlon",
    None,
    None,
    'http://www.hoeks.be',
    True,
),

#Plaats 7
'loes-mispoulier': Person(
    7,
    'Loes Mispoulier',
    'Lepelstraat 19C, maar opgegroeid in LOMMEL-BARRIER',
    28,
    'Partner Patrik Vanvelthoven',
    'Kantoorverantwoordelijke Hego Lommelb(bank en verzekeringen), Juriste',
    "Nieuw",

    "Helpt graag in de zaak van haar vriend Patrik, Coffeeshop Seasons"
    "Joggen in de zomer, fitness in de winter"
    "Lezen (krant, tijdschriften en boeken)"
    "Lekker eten, terrasje of wandeling met de familie",

    'Lokale economie, Middenstand, Infrastructuur, Financiën, ...',
    'Loes is gepassioneerd door koffie, Ze is 1m85 groot.',
    'http://www.youtube.com/watch?v=0Y9aKqawdUQ',
    "La Vita e Bella",
    None,
    None,
    None,
    True,
),

#Plaats 8,
'dominiek-van-eepoel': Person(
    8,
    'Dominiek Van Eepoel',
    'Norbert Neeckxlaan 70, 3920 Lommel',
    48,
    'Gehuwd met Marleen Plessers en vader van Stef (19), Wout (17) en Ward (14)',
    'Verantwoordelijk nieuwe productiesystemen Profel, Zaakvoerder Deves',
    "Nieuw",

    "Gepassioneerd sportliefhebber met veel aandacht voor"
    "Lommel United en Minicup."
    "Gezellig samenzijn met vrienden, skieën met de familie, Kinderen volgen in hun hobby Hobbykok en lid van een kookclub",

    'Sport, Bedrijfsleven, Financieel beleid en Onderwijs',
    'Terecht fier op zijn werk als jeugdvoorzitter van Lommel United. De club groeide van 18 naar 30 ploegen in een moderne nieuwe accomodatie en is schuldenvrij.'
    'Samen luisteren, plannen, doen, evalueren en bijsturen',
    None,
    None,
    None,
    None,
    None,
    True,
),

#NAAM:
#Favoriet youtube:	people are awesome
#Link website:	www.profel.be
#	www.deves.be
#	www.industrieonderwijs.be
#
#'''

#Plaats 9
'mieke-berghmans': Person(
    9,
    'Mieke Berghmans',
    'Rietvoornstraat 2 in WERKPLAATSEN',
    28,
    'Woont samen met vriend Robby Gysen',
    'Bediende bij Ultrapolymers Group NV, Handelsingenieur',
    "Nieuw",

    "Houdt van bioscoop, terrasjes, uit eten gaan en stapje in de wereld zetten. Supportert voor FC Motorclub",

    'Middenstand, Cultuur, Jeugd, Wijkleven, ...',
    '',
    'http://www.youtube.com/watch?v=dn7OJ_0iwBE',
    "Rocco con Buscemi",
    None,
    None,
    None,
    True,
),

#Plaats 10
'esther-vreys': Person(
    10,
    'Esther Vreys',
    'Adelbergpark, CENTRUM, Opgegroeid in de wijk HEESERBERGEN',
    25,
    'Samen met vriend Jan Geuens. Hun hond Boomer is hun grootste en langste schat',
    'Leerkracht op KA De Wingerd',
    "Nieuw",

    "Volleybal, speelt in de eerste ploeg van Lovoc, voorheen erg actief in het studentenleven en bij de Lommelse scouts. Hondenschool met haar hond Boomer",

    'Veiligheid, Sport, Cultuur, Jeugd',
    'Heeft 5 jaar gewerkt in café Zuidpool',
    'http://www.youtube.com/watch?v=5_v7QrIW0zY',
    "Isaac's Live Lipdup proposal",
    None,
    None,
    None,
    True,
),

#Plaats 11
'atabey-yildiz': Person(
    11,
    'Atabey Yildiz',
    'Geelgorsstraat 7 in Lommel BALENDIJK',
    42,
    'Gehuwd met Yildiz Hayrire, 4 kinderen (Aysun, Mustafa, Emre en Eren)',
    'Technieker bij Frankenglas NV',
    "Nieuw",

    "Basketbal, vooral om voor de kinderen te supporteren"
    "De kinderen helpen met hun huiswerk"
    "Fitness",

    'Openbare Werken, Verkeer, Sport, Cultuur en Sociale Zaken',
    'Atabey is voorzitter van de Lommelse moskeevereniging',
    None,
    None,
    None,
    None,
    None,
    False,
),

#Plaats 12
'martine-verboven': Person(
    12,
    'Martine Verboven',
    'Slinkerstraat 4 (HEIDE-HEUVEL)',
    48,
    'Gehuwd met Krupa Zygmunt, 2 kinderen (Nick en Laura)',
    'Verkoopster bij De Vossemeren',
    "Nieuw",

    "Zingen, zingen, zingen bij koor Het daghet en lid van het muzikale trio \"Three Cats and a Dog\""
    "Supporter van Lutlommel VV"
    "Koffie drinken (bij de schoonzus)",

    'Cultuur, jeugd, Wijkleven',
    'Naast haar gezin kan ze haar poezen Loes en Minoes niet missen.',
    'http://www.youtube.com/watch?v=Vh4MlX-j6oY',
    "Eddy Wally - Djippelein",
    None,
    None,
    None,
    False,
),

#Plaats 13
'chris-corens': Person(
    13,
    'Chris Corens',
    'Bergstraat, maar bouwt in de wijk KOLONIE, waar hij opgroeide',
    31,
    'Samen met Bianca Scheelen en kersverse papa van Enoah',
    'Leerkracht bij De Speling, Bijberoep als keukenontwerper en verkoper',
    "Nieuw",

    "Speler en techniektrainer jeugd bij Lutlommel VV, Liefhebber van motorcross",

    'Veiligheid, Verkeer, Sport, Onderwijs, Jeugd en Milieu',
    'Speelde met Lutlommel VV kampioen in eerste provinciale',
    None,
    None,
    None,
    None,
    None,
    True,
),

#Plaats 14,
'freddy-bantje': Person(
    14,
    'Freddy Bantje',
    'Heide 9, 3920 Lommel',
    20,
    'Ongehuwd',
    'Student',
    "Nieuw",

    "Sportliefhebber en regelmatig bezoeker van festivals, vrijwilliger bij allerlei evenementen in Lommel.",

    'Jeugd, Sport, Cultuur',
    'zeer groot liefhebber van de italiaanse keuken!'
    '"De jeugd is de stem van de toekomst"',
    'http://www.youtube.com/watch?v=1hu32aJhpC4',
    None,
    None,
    None,
    'https://www.facebook.com/freddy.bantje',
    True,
),

#Plaats 15
'eefje-beckers': Person(
    15,
    'Eefje Beckers',
    'K. Leopoldlaan 135 in LUTLOMMEL',
    35,
    'Getrouwd met Sigi Vandijck, mama van Pippa en Tobias',
    'Zelfstandige, zaakvoerder van Fermolux',
    "6 jaar Fractieleider in de Gemeenteraad",

    "Schilderen, waterskiëen, interieur familie en vrienden.",

    'Industrie en kmo, middenstand, kinderopvang en welzijn.',
    'Eefje is getrouwd in open lucht in het burgemeesterspark',
    'http://www.youtube.com/watch?v=dMH0bHeiRNg',
    "Evolution of dance",
    None,
    None,
    'http://www.fermolux.be',
    True,
),

#Plaats 16,
'anick-berghmans': Person(
    16,
    'Anick Bergmans',
    'Heide 108 in HEIDE-HEUVEL',
    31,
    'Samenwonend',
    'Zelfstandige - haar hobby is haar beroep! Optreden bij Ketnetband, kinderanimatie en sport-en danslessen.',
    "6 jaar gemeenteraadslid en afgevaardigd bestuurder AGB Sport en Recreatie",

    "Cheerleaden bij Basket K-Kontrol"
    "Lekker gaan uiteten",

    'Sport - Jeugd - Cultuur - Festiviteiten',
    'Anick gaat volgend jaar trouwen (na een bijzonder aanzoek door haar vriend Menno)'
    'Leer van gisteren, leef vandaag, droom van morgen!',
    None,
    None,
    None,
    None,
    None,
    True,
),

#Plaats 17
'kris-verduyckt': Person(
    17,
    'Kris Verduykt',
    'Schamprood 88 in LUTLOMMEL',
    35,
    'Partner van An Verspecht, Papa van Lotte en Lander',
    'Provinciaal verantwoordelijke curieus Limburg. Lic. Communicatiewetenschappen',
    "6 jaar gemeenteraadslid en 6 jaar Schepen, momenteel eerste Schepen van Sport, Mobiliteit, Jeugd en Lommel Leeft",

    "(Café)voetbal bij FC Pinal"
    "Orientatielopen, geocaching en joggen"
    "Organiseren van klapkwiss, optredens en openluchtfilms"
    "Houdt van reizen, muziek, film en vooral goed leven!",

    'Sport, Vrije Tijd, Ruimtelijke Ordening, Cultuur, ...',
    'Als kwisser nam Kris al deel aan twee TV-kwissen: de Pappenheimers en de Canvascrack.',
    'http://www.youtube.com/watch?v=7aYMQmdHVp4',
    "Spot orienteering",
    None,
    None,
    'http://www.kriskijktvooruit.be',
    True,
),

#Plaats 18
'liesbet-vanwelsenaers': Person(
    18,
    'Liesbet Vanwelsenaers',
    'Pijnvenstraat 49 in KERKHOVEN',
    35,
    'Gehuwd met Pietro Fontana. Mama van Iva (8), Zita (7) en Maysa (0,5)',
    'Psychologe / diensthoofd sociale dienst De Voorzorg',
    "12 jaar Schepen, momenteel Schepen van Toerisme, Sociale Zaken, internationale betrekkingen...",

    "Leuke dingen doen met het gezin, lezen"
    "Activiteiten organiseren met curieus Kerkhoven zoals Kerkhoven Speelt, ... Lommel rockt",

    'Sociale Zaken en welzijn, cultuur, sport, ...',
    'Liesbet is de fiere meter van Idem Dito',
    None,
    None,
    None,
    None,
    None,
    True,
),

#Plaats 19,
'rina-ven': Person(
    19,
    'Rina Ven',
    'Grote Fosséstraat 9 in Lommel KOLONIE',
    54,
    'gehuwd met Charles Poets. mama van Gert en Jannick',
    'Maatschappelijk assistente',
    "12 jaar schepen milieu, natuur, openbare werken, dierenwelzijn, begraafplaatsen",

    "fietsen, wandelen,lezen, gezellig samenzijn met het gezin",

    'milieu, natuur, welzijn, cultuur,',
    'Rina stond aan de wieg van "Bosland"',
    'http://www.youtube.com/watch?feature=player_embedded&v=qXo3NFqkaRM#!',
    'Husky Dog Talking "I love you"',
    None,
    None,
    None,
    False,
),

#Plaats 20
'jean-kuyken': Person(
    20,
    'Jean Kuyken',
    'Beemdstraat 5 in LUTLOMMEL',
    60,
    'Gehuwd met Angele Verdonck. Vader van Tom en Inge',
    'Zelfstandig frituuruitbater. Vrijwillig brandweerman',
    "9 jaar gemeenteraadslid, 3 jaar Schepen van Stadswerken",

    "Kijkt graag als toeschouwer naar vele sporten, vooral voetbal.",

    'Verkeer, Milieu, Openbare Werken, Sport en Veiligheid',
    'Frituur Jean is een van de oudste frituren in Lommel',
    'http://www.youtube.com/watch?v=U3af0HmDq1o',
    "Brandweer Lommel heeft nieuwe autopomp",
    None,
    None,
    None,
    True,
),

#Plaats 21
'jan-swinnen': Person(
    21,
    'Jan Swinnen',
    'Norbert Neeckxlaan 78 in LOMMEL CENTRUM',
    61,
    'Gehuwd met psychologe Rita Vanhove'
    'Papa van Charlotte en Marie'
    'Opa van Floris',
    'Huisarts en voorzitter van VZW De Drempel groepspraktijk in de Ruiterijstraat',
    "21 jaar Schepen, momenteel Schepen van Cultuur, Bibliotheek, AGB Sport & Recreatie en volwassenenonderwijs",

    "Muziek (tango dansen, ...)"
    "Kunst en cultuur en vooral ook fotografie",

    'Infrastructuur (uitbouw sportinfrastructuur), Sport, Cultuur Sociale Zaken en welzijn',
    'In de jaren \'70 actief als arts in Mozambique en nog steeds actief in het Lommels steuncomité voor Mozambique',
    '',
    "Lead India - The Tree",
    None,
    None,
    None,
    True,
),
#Ervaring + goesting = uw stem

#Plaats 22
'jean-lavreysen': Person(
    22,
    'Jean Lavreysen',
    'Hertog Janplein 22D',
    61,
    'Gehuwd met Vera Mentens, 2 dochters',
    'Ere-directeur Provinciaal Opleidingscentrum voor Politie, Brandweer en Ambulanciers',
    "30 jaar Gemeenteraadslid waarvan 22 jaar als Schepen van Financiën en 4 jaar OCMW-voorzitter",

    "Fietsen"
    "Wandelen bij Milieu 2000"
    "Voorzitter van Kattenbos Sport"
    "curieus Kattenbos",

    'Financiën, Senioren, Vrije Tijd',
    'Heeft dit jaar samen met Vera al meer dan 6.000 km. gefietst (zoals met de actie Fietsen tegen Kanker)',
    'http://www.youtube.com/watch?v=KeiZDXf0t9o',
    "Fietsen in Spanje",
    None,
    None,
    None,
    True,
),

#Plaats 23
'joke-loomans': Person(
    23,
    'Joke Loomans',
    'Eviestraat 24 in KATTENBOS',
    40,
    'Getrouwd met Kim Vandenboer en mama van. Lise-Marie, Kobe, Jules en Amelie',
    'Bediende. Lic. Vertaler Engels-Spaans',
    "9 jaar Schepen, 3 jaar Gemeenteraadslid",

    "Badminton met curieus Kattenbos"
    "Reizen en skiën met het gezin"
    "Schilderen"
    "Gaan supporteren voor het voetbal van de kids",

    'Economie, toerisme, middenstand en Kattenbos',
    'Joke heeft enkele jaren in Spanje gewoond en spreekt vloeiend Spaans',
    'http://www.youtube.com/watch?v=W96XquwmV8o',
    "David Guetta @ tomorrowland",
    None,
    None,
    None,
    True,
),

#Plaats 24
'elly-vanbrabant': Person(
    24,
    'Elly Vanbrabant',
    'Oude Diestersebaan in KATTENBOS',
    47,
    'Partner Frank Lourdaux. 3 kinderen: Jasper, Amber en Merel',
    'Praktische draaischijf en verantwoordelijk voor lekenwerking in het klooster van Kattenbos',
    "Nieuw",

    "Joggen  (fervent deelneemster aan teutenbosloop)"
    "Badminton met curieus Kattenbos"
    "Koken en dus etentjes met familie of vrienden"
    "Fan van wielrennen (Een bezoekje aan de tour vind ik het einde, de Lommelse profronde ook)",

    'Welzijn, Sport, Cultuur en Vrije Tijd',
    'Kijkt recht op het treinspoor en houdt van treinen',
    'http://www.youtube.com/watch?v=X9whxWNI7bE',
    "Susan Boyles first audition",
    None,
    None,
    None,
    True,
),

#Plaats 25
'erik-maes': Person(
    25,
    'Eric Maes',
    'Scheepvaartstraat 6 in STEVENSVENNEN',
    49,
    'Gehuwd met Elly Bogaerts. Vader van Nathalie en Ellen',
    'Arbeider bij Sibelco',
    "Nieuw",

    "Voorzitter van voetbalploeg FC Motorclub. Voetbal en jagen zijn zijn passies.",

    'Wijkleven, Sport, Veiligheid, Sociale Zaken',
    'Zijn dochter Ellen baat een kinderopvang uit in Stevensvennen',
    'http://www.youtube.com/watch?v=s2tGPoG8LVg',
    "Belgium vs USSR - Mexico 1986",
    None,
    None,
    None,
    True,
),

#Plaats 26
'veerle-baert': Person(
    26,
    'Veerle Baert',
    'Zwanenstraat 20 in Lommel KOLONIE',
    40,
    'Gehuwd met Tom de Kort en mama van Elke (19), Shanti (16) en Lara (15)',
    'Loketbediende bij De Voorzorg in Lommel',
    "Nieuw",

    "Soprtwedstrijden van de kinderen gaan bekijken. Fietsen met de koersfiets",

    'Sociale Zaken en Welzijn',
    'sportieve kinderen: Elke geeft tennisles, Lara is judoka en Shanti tennist',
    'http://www.youtube.com/watch?v=c8SL8vPr3a8',
    "Talent uit eigen tent (A. Delamazuretrio)",
    None,
    None,
    None,
    True,
),

#Plaats 27
'sally-de-jong': Person(
    27,
    'Sally De jong',
    'Vreyshorring 194 in CENTRUM',
    31,
    'vrijgezel',
    'Verpleegkundige',
    "Nieuw",

    "Sally is lid van de Neerpeltse tennisclub en speelt ook badminton. "
    "Ze houdt van terrasjes, uit eten gaan met vrienden en familie.",

    'Sport, gezondheid en welzijn.',
    'Sally haar grootste schat heet "Einstein" en is een mini maltezer.',
    'http://www.youtube.com/watch?v=dnp2gHMecEU',
    "Najib Amhali",
    None,
    None,
    None,
    True,
),

#Plaats 28
'ronny-geysen': Person(
    28,
    'Ronny Geysen',
    'Sparstraat 12, HEIDE-HEUVEL',
    49,
    'Ongehuwd',
    'Bediende bij Philips Turnhout',
    "6 jaar gemeenteraadslid",

    "Mountainbike bij Bike Action Team Lommel"
    "Bestuurslid bij supportersclub Heuvelhof, zijn hart klopt groen en wit"
    "Houdt van het Lommelse karnaval"
    "Citytrips",

    'Milieu, Sport, Ruimtelijk Ordening, Lommel Leeft',
    'Ronny is de huidige voorzitter van de Sportraad',
    'http://www.youtube.com/watch?v=l457Eg33qJ4&feature=fvwrel',
    "Lassie",
    None,
    None,
    None,
    True,
),

#plaats 29
'danny-huijsmans': Person(
    29,
    'Danny Huijsmans',
    'Kanaalstraat 19, KERKHOVEN',
    57,
    'Gehuwd met Martien De Vrieze. Vader van Katelijne en Maarten',
    'Directeur Basisschool Sint-Jan Kerkhoven. Lid van het DB van de Directiecommissie Kath. Onderwijs',
    "Nieuw",

    "Voorzitter bij muziekateliers Lommel"
    "Skiën en films kijken"
    "Supporter van Johan Vansummeren en Lommel United"
    "Lid van de Ervaringsgerichte contactgroep Limburg",

    'Democratie, Verkeer, Cultuur, Sociale Zaken, Onderwijs',
    'Danny gaat al jaren mee tappen op Pukkelpop met de vereniging Lommel Rockt!',
    '',
    None,
    'http://twitter.com/huijsmansdanny',
    'https://www.facebook.com/huijsmansdanny',
    'http://www.sintjan-lommel.be',
    True,
),

#Plaats 30,
'fons-haagdoren': Person(
    30,
    'Fons Haagdoren',
    'Stortstraat 16 in Lommel-BARRIER',
    69,
    'Gehuwd met Christiane Swerts. Heeft 1 zoon Philip (trainer Lommel United',
    'Pensioen',
    "18 jaar Gemeenteraadslid waarvan 13 jaar als Schepen",

    "Tuinieren, sporten en sport kijken"
    "Organiseren van sportevenementen in de stad Lommel"
    "(profronde, superprestige Biljart, ...)",

    'Sport, senioren',
    'Fons haalde ooit een cap als Rode Duivel',
    'http://www.youtube.com/watch?v=i48FDeuQCNI',
    "Profronde Lommel V03",
    None,
    None,
    None,
    True,
),

#Plaats 31
'francois-timmermans': Person(
    31,
    'Francois Timmermans',
    'Kloostersstraat 216 in LUTLOMMEL',
    64,
    'Gehuwd met Thea',
    'Bruggepensioneerde',
    "24 jaar Gemeenteraadslid waarvan 14 jaar als Schepen en OCMW-voorzitter",

    "Echte voetballiefhebber"
    "Voorzitter voetbalclub FC Germinal"
    "Penningmeester Verenigde LutlommelarenActief in de buurtwerking",

    'Sport - Senioren - Sociale Zaken',
    'Francois werkte liefst 35 jaar bij De Voorzorg',
    'http://www.youtube.com/watch?v=uw-QCLbSedQ',
    "Hades - Lutlommel VV 1-5",
    None,
    None,
    None,
    True,
)}




# Quick hack to have them as a sorted list, its a list of tuples (key,value)

#sorted(d.items(), key=itemgetter(1))
#input.sort(lambda x,y : cmp(x['name'], y['name']))
#sorted_persons = sorted(persons.items(), key=itemgetter(0))
persons_sorted = sorted(persons.items(), key=lambda (k, v): float(v.place))

