# -- coding: utf-8 --

class Person:
    def __init__(self, place, name, address, age, family, profession, career,
                 leisure_time, interests, fun_fact, youtube, youtube_title, twitter, facebook, website,
                 pic_youth, slogan, youtube_promo, gender):
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
        self.slogan = slogan
        self.youtube_promo = youtube_promo
        self.gender = gender

persons = {
# Plaats 1
'peter-vanvelthoven': Person(
    1,
    'Peter Vanvelthoven',
    'Kerkstraat 32A in Lommel <strong>Centrum</strong>',
    49,
    'gehuwd met Ingrid en twee kinderen:  Nathalie (18) en Sam (14)',
    'Burgemeester en volksvertegenwoordiger, Rechten gestudeerd',

    "<li>Deputé van Limburg (1995)</li>"
    "<li>Vlaams volksvertegenwoordiger (1995-1999)</li>"
    "<li>Federaal volksvertegenwoordiger (1999-2003)</li>"
    "<li>Staatssecretaris (2003-2005), minister (2005-2007)</li>"
    "<li>Federaal volksvertegenwoordiger (2007)</li>"
    "<li>en Burgemeester van Lommel sedert 2006</li>",

    "<li>Heeft vroeger veel gebasket en tennis gespeeld. Nu kijkt hij vooral naar het basketbal van de kinderen. </li>"
    "<li>Voor de rest af en toe een terrasje in Lommel. </li>"
    "<li>Kan genieten van een avond thuis met een goeie film</li>",

    'In heel veel dingen geïnteresseerd, als burgemeester komt dat goed van pas',
    'Gek van Amerikaans basketbal',
    'http://www.youtube.com/watch?v=4VLmJ43fHpM&feature=results_main&playnext=1&list=PL11748D4EA7A9D1CE',
    None,
    None,
    "https://www.facebook.com/pvanvelthoven",
    'http://www.petervanvelthoven.be',
    True,
    "Geef het beste van jezef, ook aan anderen",
    "http://www.youtube.com/embed/lBHA9mYkzzM",
    "M",
),

# Plaats 2
'an-vanden-boer': Person(
    2,
    'An Vander Boer',
    'Vreyshorring 15A in Lommel <strong>Centrum</strong>',
    26,
    'Vrijgezel',
    'Advocaat',

    "<li>Nieuw</li>",

    "<li>An speelt tennis bij LTC waar ze ook bestuurslid is</li>"
    "<li>Ze speelt basket bij K-Kontrol Lommel</li>"
    "<li>Houdt van films, lezen en kwissen bij quizploeg Bruudruuster</li>",

    'Sport, verkeer, onderwijs, welzijn',
    'Beide  grootvaders zaten ooit in de politiek',
    'http://www.youtube.com/watch?v=-ZJDNSp1QJA',
    'The piano - amazing short',
    None,
    None,
    'http://www.advoclommel.be',
    True,
    "Energiek aan de slag voor onze stad",
    "http://www.youtube.com/embed/tBVEMu-os08",
    "F",
),

#Plaats 3
'walter-cremers': Person(
    3,
    'Walter Cremers',
    'Peter Aertsstraat 10 in Lommel <strong>Barrier</strong>',
    56,
    'Gehuwd met Christiane Poorters<br/>'
    'Vader van Jef, die getrouwd is met Heidi Geysmans en haar kinderen Annisce en Celince',
    'Landmeter / ambtenaar',

    "<li>LOMMEL: 20 jaar Schepen, 1 jaar Wnd Burgemeester</li>"
    "<li>PROVINCIE: 18 jaar provincieraadslid en momenteel 3 jaar gedeputeerde </li>",

    "<li>Wielertoerist en overtuigd ventourist, Wandelen</li>",

    'Ruimtelijke Ordening, Sport, Dierenwelzijn, Mobiliteit',
    'Walter was 9 jaar lang de voorzitter van Interelectra',
    'http://www.youtube.com/watch?v=nfL8RGV-t2U&feature=related',
    "Fragment De Parelvissers",
    None,
    "http://www.facebook.com/walter.cremers",
    None,
    True,
    "Ruimte maken, is werken aan oplossingen",
    "http://www.youtube.com/embed/tXbsLeDvIdA",
    "M",
),

#Plaats 4
'jasmine-vangrieken': Person(
    4,
    'Jasmine Vangrieken',
    'Weidestraat 45 in <strong>Lutlommel</strong>',
    28,
    'Samenwonend met vriend Johan Vansummeren. ',
    'Orthopedagoge',

    "<li>6 jaar Gemeenteraadslid</li>",

    "<li>Wielrennen, zwemmen, lopen</li>"
    "<li>Ik ga graag naar alle sporten kijken</li>"
    "<li>Filmpje mee pikken, terrasje doen</li>"
    "<li>Lekker uit eten gaan</li>",

    'Jeugd, sport, sociale zaken en welzijn',
    'Jasmine deed zelf jaren aan topsport (zwemmen) en trouwt in oktober',
    'http://www.youtube.com/watch?v=Q3Nsn-reFSc',
    "Laatste kilometer Johan Vansummeren",
    "minavangrieken",
    None,
    None,
    True,
    "Sport en kwaliteit. Hand in hand.",
    "http://www.youtube.com/embed/49xQs7K9YBE",
    "F",
),

#Plaats 5
'rita-phlippo': Person(
    5,
    'Rita Phlippo',
    'Kerkhovensesteenweg 453 in <strong>Kerkhoven</strong>',
    46,
    'Gescheiden en 2 kinderen Nick (18) en Chloé (15)',
    'Apothekeres',

    "<li>6 jaar gemeenteraadslid en zetelt in het bestuurscomité van Infrax</li>",

    "<li>Mensen bewust maken over hun gezondheid via preventie</li>"
    "<li>Salsadansen bij Salsa2You in Lommel</li>"
    "<li>Reizen, contact met andere culturen</li>"
    "<li>Fietsen en up to date blijven met mijn pubers</li>",

    'Sociale Zaken, welzijn en gezondheid, middenstand',
    'Rita organiseert al enkele jaren met veel succes gezondheidsavonden in het raadhuis.',
    'http://www.youtube.com/watch?v=Vk7eoKNrK8M',
    "The World Book of Happiness",
    None,
    "https://www.facebook.com/rita.phlippo",
    'http://www.apotheekphlippo.be',
    True,
    "Gezonde ambitie voor Lommel",
    "http://www.youtube.com/embed/MFIfcHaq5bA",
    "F",
),

#Plaats 6
'johan-hoeks': Person(
    6,
    'Johan Hoeks',
    'Rijkschoolstraat, <strong>Centrum</strong>',
    53,
    'Gehuwd met Vera Berben, vader van Maarten en "pake" van Xander en Elias',
    'Bedrijfsleider van Hoeks Verhuizingen en Kuismasters.com',

    "<li>Nieuw</li>",

    "<li>Bestuurslid van service club '51 t' Zand</li>"
    "<li>Hoofdsponsor van de Lommelse triatlon en gepassioneerd door deze sport Golfen</li>",

    'Lokale economie, Veiligheid, Sport, Middenstand',
    '',
    'http://www.youtube.com/watch?v=Aank3dbGZ44',
    "Hoeks Triatlon",
    None,
    "http://www.facebook.com/johan.hoeks.1",
    'http://www.hoeks.be',
    True,
    "Samen met een ploeg harde werkers",
    "http://www.youtube.com/embed/ahtfIKr_o9k",
    "M",
),

#Plaats 7
'loes-mispoulier': Person(
    7,
    'Loes Mispoulier',
    'Lepelstraat 19C, maar opgegroeid in <strong>Lommel-Barrier</strong>',
    28,
    'Partner Patrik Vanvelthoven',
    'Kantoorverantwoordelijke Hego Lommel (bank en verzekeringen), Juriste',

    "<li>Nieuw</li>",

    "<li>Helpt graag in de zaak van haar vriend Patrik, Coffeeshop Seasons</li>"
    "<li>Joggen in de zomer, fitness in de winter</li>"
    "<li>Lezen (krant, tijdschriften en boeken)</li>"
    "<li>Lekker eten, terrasje of wandeling met de familie</li>",

    'Lokale economie, Middenstand, Infrastructuur, Financiën, ...',
    'Loes is gepassioneerd door koffie, Ze is 1m85 groot.',
    'http://www.youtube.com/watch?v=0Y9aKqawdUQ',
    "La Vita e Bella",
    None,
    "http://www.facebook.com/loes.mispoulier",
    None,
    True,
    "Samen hard aan de toekomst werken",
    "http://www.youtube.com/embed/PE-kUy-5OT0",
    "F",
),

#Plaats 8,
'dominiek-van-eepoel': Person(
    8,
    'Dominiek Van Eepoel',
    'Norbert Neeckxlaan 70, 3920 Lommel',
    48,
    'Gehuwd met Marleen Plessers en vader van Stef (19), Wout (17) en Ward (14)',
    'Verantwoordelijk nieuwe productiesystemen Profel, Zaakvoerder Deves',

    "<li>Nieuw</li>",

    "<li>Gepassioneerd sportliefhebber met veel aandacht voor</li>"
    "<li>Lommel United en Minicup</li>"
    "<li>Gezellig samenzijn met vrienden, skieën met de familie, Kinderen volgen in hun hobby Hobbykok en lid van een kookclub</li>",

    'Sport, Bedrijfsleven, Financieel beleid en Onderwijs',
    'Terecht fier op zijn werk als jeugdvoorzitter van Lommel United. De club groeide van 18 naar 30 ploegen in een moderne nieuwe accomodatie en is schuldenvrij',
    None,
    None,
    None,
    "http://www.facebook.com/dominiek.vaneepoel",
    None,
    True,
    "Samen luisteren, plannen, doen, evalueren en bijsturen",
    "http://www.youtube.com/embed/NMXFaL3t-To",
    "M",
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
    'Rietvoornstraat 2 in <strong>Werkplaatsen</strong>',
    28,
    'Woont samen met vriend Robby Gysen',
    'Bediende bij Ultrapolymers Group NV, Handelsingenieur',

    "<li>Nieuw</li>",

    "<li>Houdt van bioscoop, terrasjes</li>"
    "<li>uit eten gaan en stapje in de wereld zetten</li>"
    "<li>Supportert voor FC Motorclub</li>",

    'Middenstand, Cultuur, Jeugd, Wijkleven, ...',
    '',
    'http://www.youtube.com/watch?v=dn7OJ_0iwBE',
    "Rocco con Buscemi",
    None,
    "http://www.facebook.com/mieke.berghmans.1",
    None,
    True,
    "Goede jobs in ons eigen Lommel",
    "http://www.youtube.com/embed/blQUU4R8_Dw",
    "F",
),

#Plaats 10
'esther-vreys': Person(
    10,
    'Esther Vreys',
    'Adelbergpark, <strong>Centrum</strong>, Opgegroeid in de wijk <strong>Heeserbergen</strong>',
    25,
    'Samen met vriend Jan Geuens. Hun hond Boomer is hun grootste en langste schat',
    'Leerkracht op KA De Wingerd',

    "<li>Nieuw</li>",

    "<li>Volleybal, speelt in de eerste ploeg van Lovoc</li>"
    "<li>voorheen erg actief in het studentenleven en bij de Lommelse scouts</li>"
    "<li>Hondenschool met haar hond Boomer</li>",

    'Veiligheid, Sport, Cultuur, Jeugd',
    'Heeft 5 jaar gewerkt in café Zuidpool',
    'http://www.youtube.com/watch?v=5_v7QrIW0zY',
    "Isaac's Live Lipdup proposal",
    None,
    "http://www.facebook.com/esther.vreys",
    None,
    True,
    "Mensen staan voor mij centraal",
    "http://www.youtube.com/embed/HV7CD-TkrVM",
    "F",
),

#Plaats 11
'atabey-yildiz': Person(
    11,
    'Atabey Yildiz',
    'Geelgorsstraat 7 in Lommel <strong>Balendijk</strong>',
    42,
    'Gehuwd met Yildiz Hayrire, 4 kinderen (Aysun, Mustafa, Emre en Eren)',
    'Technieker bij Frankenglas NV',

    "<li>Nieuw</li>",

    "<li>Basketbal, vooral om voor de kinderen te supporteren</li>"
    "<li>De kinderen helpen met hun huiswerk</li>"
    "<li>Fitness</li>",

    'Openbare Werken, Verkeer, Sport, Cultuur en Sociale Zaken',
    'Atabey is voorzitter van de Lommelse moskeevereniging',
    None,
    None,
    None,
    None,
    None,
    False,
    "Iedereen telt mee, iedereen moet kansen krijgen",
    "http://www.youtube.com/embed/XkjmKkMbsgU",
    "M",
),

#Plaats 12
'martine-verboven': Person(
    12,
    'Martine Verboven',
    'Slinkerstraat 4 <strong>Heide-Heuvel</strong>',
    48,
    'Gehuwd met Krupa Zygmunt, 2 kinderen (Nick en Laura)',
    'Verkoopster bij De Vossemeren',

    "<li>Nieuw</li>",

    "<li>Zingen, zingen, zingen bij koor Het daghet en lid van het muzikale trio \"Three Cats and a Dog\"</li>"
    "<li>Supporter van Lutlommel VV</li>"
    "<li>Koffie drinken (bij de schoonzus)</li>",

    'Cultuur, jeugd, Wijkleven',
    'Naast haar gezin kan ze haar poezen Loes en Minoes niet missen.',
    'http://www.youtube.com/watch?v=Vh4MlX-j6oY',
    "Eddy Wally - Djippelein",
    None,
    None,
    None,
    False,
    "Lommel... als muziek in mijn oren",
    "http://www.youtube.com/embed/Osppk3Qwckk",
    "F",
),

#Plaats 13
'chris-corens': Person(
    13,
    'Chris Corens',
    'Bergstraat, maar bouwt in de wijk <strong>Kolonie</strong>, waar hij opgroeide',
    31,
    'Samen met Bianca Scheelen en kersverse papa van Enoah',
    'Leerkracht bij De Speling, Bijberoep als keukenontwerper en verkoper',

    "<li>Nieuw</li>",

    "<li>Speler en techniektrainer jeugd bij Lutlommel VV</li>"
    "<li>Liefhebber van motorcross</li>",

    'Veiligheid, Verkeer, Sport, Onderwijs, Jeugd en Milieu',
    'Speelde met Lutlommel VV kampioen in eerste provinciale',
    None,
    None,
    None,
    None,
    None,
    True,
    "In de voetsporen van mijn grootvader...",
    "http://www.youtube.com/embed/HRTHSWzI82c",
    "M",
),

#Plaats 14,
'freddy-bantje': Person(
    14,
    'Freddy Bantje',
    'Heide 9, 3920 Lommel',
    20,
    'Ongehuwd',
    'Student',

    "<li>Nieuw</li>",

    "<li>Sportliefhebber en regelmatig bezoeker van festivals</li>"
    "<li>vrijwilliger bij allerlei evenementen in Lommel</li>",

    'Jeugd, Sport, Cultuur',
    'zeer groot liefhebber van de italiaanse keuken!',
    'http://www.youtube.com/watch?v=1hu32aJhpC4',
    None,
    None,
    "http://www.facebook.com/freddy.bantje",
    None,
    True,
    "Jong? Ik ook",
    "http://www.youtube.com/embed/IyZfr_UWVV0",
    "M",
),

#Plaats 15
'eefje-beckers': Person(
    15,
    'Eefje Beckers',
    'K. Leopoldlaan 135 in <strong>Lutlommel</strong>',
    35,
    'Getrouwd met Sigi Vandijck, mama van Pippa en Tobias',
    'Zelfstandige, zaakvoerder van Fermolux',

    "<li>6 jaar Fractieleider in de Gemeenteraad</li>",

    "<li>Schilderen</li>"
    "<li>waterskiëen</li>"
    "<li>interieur</li>"
    "<li>familie en vrienden</li>",

    'Industrie en kmo, middenstand, kinderopvang en welzijn.',
    'Eefje is getrouwd in open lucht in het burgemeesterspark',
    'http://www.youtube.com/watch?v=dMH0bHeiRNg',
    "Evolution of dance",
    None,
    "http://www.facebook.com/eefje.beckers.5",
    'http://www.fermolux.be',
    True,
    "Een stad besturen is durven beslissen",
    "http://www.youtube.com/embed/Z62z87t9BQ8",
    "F",
),

#Plaats 16,
'anick-berghmans': Person(
    16,
    'Anick Bergmans',
    'Heide 108 in <strong>Heide-Heuvel</strong>',
    31,
    'Samenwonend',
    'Zelfstandige - haar hobby is haar beroep! Optreden bij Ketnetband, kinderanimatie en sport-en danslessen.',

    "<li>6 jaar gemeenteraadslid en afgevaardigd bestuurder AGB Sport en Recreatie</li>",

    "<li>Cheerleaden bij Basket K-Kontrol</li>"
    "<li>Lekker gaan uiteten</li>",

    'Sport - Jeugd - Cultuur - Festiviteiten',
    'Anick gaat volgend jaar trouwen (na een bijzonder aanzoek door haar vriend Menno)',
    None,
    None,
    None,
    "http://www.facebook.com/anick.berghmans",
    None,
    True,
    "Leer van gisteren, leef vandaag, droom van morgen!",
    "http://www.youtube.com/embed/Mdpey-95QiE",
    "F",
),

#Plaats 17
'kris-verduyckt': Person(
    17,
    'Kris Verduykt',
    'Schamprood 88 in <strong>Lutlommel</strong>',
    35,
    'Partner van An Verspecht, Papa van Lotte en Lander',
    'Provinciaal verantwoordelijke curieus Limburg. Lic. Communicatiewetenschappen',

    "<li>6 jaar gemeenteraadslid</li>"
    "<li>6 jaar Schepen, momenteel eerste Schepen van Sport, Mobiliteit, Jeugd en Lommel Leeft</li>",

    "<li>(Café)voetbal bij FC Pinal</li>"
    "<li>Orientatielopen, geocaching en joggen</li>"
    "<li>Organiseren van klapkwiss, optredens en openluchtfilms</li>"
    "<li>Houdt van reizen, muziek, film en vooral goed leven!</li>",

    'Sport, Vrije Tijd, Ruimtelijke Ordening, Cultuur, ...',
    'Als kwisser nam Kris al deel aan twee TV-kwissen: de Pappenheimers en de Canvascrack.',
    'http://www.youtube.com/watch?v=7aYMQmdHVp4',
    "Spot orienteering",
    None,
    "http://www.facebook.com/krisverduyckt",
    'http://www.kriskijktvooruit.be',
    True,
    "Met een frisse kop vol ideeën",
    "http://www.youtube.com/embed/8XeAH_d7Fys",
    "M",
),

#Plaats 18
'liesbet-vanwelsenaers': Person(
    18,
    'Liesbet Vanwelsenaers',
    'Pijnvenstraat 49 in <strong>Kerkhoven</strong>',
    35,
    'Gehuwd met Pietro Fontana. Mama van Iva (8), Zita (7) en Maysa (0,5)',
    'Psychologe / diensthoofd sociale dienst De Voorzorg',

    "<li>12 jaar Schepen, momenteel Schepen van Toerisme, Sociale Zaken, internationale betrekkingen...</li>",

    "<li>Leuke dingen doen met het gezin, lezen</li>"
    "<li>Activiteiten organiseren met curieus Kerkhoven zoals Kerkhoven Speelt, ... Lommel rockt</li>",

    'Sociale Zaken en welzijn, cultuur, sport, ...',
    'Liesbet is de fiere meter van Idem Dito',
    None,
    None,
    None,
    "http://www.facebook.com/lies.vanwelsenaers",
    None,
    True,
    "'Be' the change you want to 'see' in the world",
    "http://www.youtube.com/embed/aa1CPP_PjNU",
    "F",
),

#Plaats 19,
'rina-ven': Person(
    19,
    'Rina Ven',
    'Grote Fosséstraat 9 in Lommel <strong>Kolonie</strong>',
    54,
    'gehuwd met Charles Poets. mama van Gert en Jannick',
    'Maatschappelijk assistente',

    "<li>12 jaar schepen milieu, natuur, openbare werken, dierenwelzijn, begraafplaatsen</li>",

    "<li>fietsen</li>"
    "<li>wandelen</li>"
    "<li>lezen</li>"
    "<li>gezellig samenzijn met het gezin</li>",

    'milieu, natuur, welzijn, cultuur,',
    'Rina stond aan de wieg van "Bosland"',
    'http://www.youtube.com/watch?feature=player_embedded&v=qXo3NFqkaRM#!',
    'Husky Dog Talking "I love you"',
    None,
    None,
    None,
    False,
    "Genieten van onze prachtige, groene natuur en bossen",
    "http://www.youtube.com/embed/zF7lmkzL9Oc",
    "F",
),

#Plaats 20
'jean-kuyken': Person(
    20,
    'Jean Kuyken',
    'Beemdstraat 5 in <strong>Lutlommel</strong>',
    60,
    'Gehuwd met Angele Verdonck. Vader van Tom en Inge',
    'Zelfstandig frituuruitbater. Vrijwillig brandweerman',

    "<li>9 jaar gemeenteraadslid</li>"
    "<li>3 jaar Schepen van Stadswerken</li>",

    "<li>Kijkt graag als toeschouwer naar vele sporten, vooral voetbal</li>",

    'Verkeer, Milieu, Openbare Werken, Sport en Veiligheid',
    'Frituur Jean is een van de oudste frituren in Lommel',
    'http://www.youtube.com/watch?v=U3af0HmDq1o',
    "Brandweer Lommel heeft nieuwe autopomp",
    None,
    "http://www.facebook.com/jean.kuyken",
    None,
    True,
    "Kleine of grote problemen, op mij kan je tellen",
    "http://www.youtube.com/embed/7vefCOrV89w",
    "M",
),

#Plaats 21
'jan-swinnen': Person(
    21,
    'Jan Swinnen',
    'Norbert Neeckxlaan 78 in Lommel <strong>Centrum</strong>',
    61,
    'Gehuwd met psychologe Rita Vanhove<br/>'
    'Papa van Charlotte en Marie<br/>'
    'Opa van Floris<br/>',
    'Huisarts en voorzitter van VZW De Drempel groepspraktijk in de Ruiterijstraat',

    "<li>21 jaar Schepen, momenteel Schepen van Cultuur, Bibliotheek, AGB Sport & Recreatie en volwassenenonderwijs</li>",

    "<li>Muziek (tango dansen, ...)</li>"
    "<li>Kunst en cultuur en vooral ook fotografie</li>",

    'Infrastructuur (uitbouw sportinfrastructuur), Sport, Cultuur Sociale Zaken en welzijn',
    'In de jaren \'70 actief als arts in Mozambique en nog steeds actief in het Lommels steuncomité voor Mozambique',
    '',
    "Lead India - The Tree",
    None,
    "http://www.facebook.com/jan.swinnen.9",
    None,
    True,
    "Met verbeelding kom je overal",
    "http://www.youtube.com/embed/DZU-lFjgLUo",
    "M",
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

    "<li>30 jaar Gemeenteraadslid waarvan 22 jaar als Schepen van Financiën en 4 jaar OCMW-voorzitter</li>",

    "<li>Fietsen</li>"
    "<li>Wandelen bij Milieu 2000</li>"
    "<li>Voorzitter van Kattenbos Sport</li>"
    "<li>curieus Kattenbos</li>",

    'Financiën, Senioren, Vrije Tijd',
    'Heeft dit jaar samen met Vera al meer dan 6.000 km. gefietst (zoals met de actie Fietsen tegen Kanker)',
    'http://www.youtube.com/watch?v=KeiZDXf0t9o',
    "Fietsen in Spanje",
    None,
    None,
    None,
    True,
    "Lommel. Altijd het beste is goed genoeg!",
    "http://www.youtube.com/embed/_gCztAIhQJg",
    "M",
),

#Plaats 23
'joke-loomans': Person(
    23,
    'Joke Loomans',
    'Eviestraat 24 in <strong>Kattenbos</strong>',
    40,
    'Getrouwd met Kim Vandenboer en mama van. Lise-Marie, Kobe, Jules en Amelie',
    'Bediende. Lic. Vertaler Engels-Spaans',

    "<li>9 jaar Schepen</li>"
    "<li>3 jaar Gemeenteraadslid</li>",

    "<li>Badminton met curieus Kattenbos</li>"
    "<li>Reizen en skiën met het gezin</li>"
    "<li>Schilderen</li>"
    "<li>Gaan supporteren voor het voetbal van de kids</li>",

    'Economie, toerisme, middenstand en Kattenbos',
    'Joke heeft enkele jaren in Spanje gewoond en spreekt vloeiend Spaans',
    'http://www.youtube.com/watch?v=W96XquwmV8o',
    "David Guetta @ tomorrowland",
    None,
    None,
    None,
    True,
    "Werk in eigen streek, daar werk ik voor",
    "http://www.youtube.com/embed/KFyaVEm-2MQ",
    "F",
),

#Plaats 24
'elly-vanbrabant': Person(
    24,
    'Elly Vanbrabant',
    'Oude Diestersebaan in <strong>Kattenbos</strong>',
    47,
    'Partner Frank Lourdaux. 3 kinderen: Jasper, Amber en Merel',
    'Praktische draaischijf en verantwoordelijk voor lekenwerking in het klooster van Kattenbos',

    "<li>Nieuw</li>",

    "<li>Joggen  (fervent deelneemster aan teutenbosloop)</li>"
    "<li>Badminton met curieus Kattenbos</li>"
    "<li>Koken en dus etentjes met familie of vrienden</li>"
    "<li>Fan van wielrennen (Een bezoekje aan de tour vind ik het einde, de Lommelse profronde ook)</li>",

    'Welzijn, Sport, Cultuur en Vrije Tijd',
    'Kijkt recht op het treinspoor en houdt van treinen',
    'http://www.youtube.com/watch?v=X9whxWNI7bE',
    "Susan Boyles first audition",
    None,
    None,
    None,
    True,
    "Op het juiste spoor... met Lijst Burgemeester",
    "http://www.youtube.com/embed/hNiXVwY5xb0",
    "F",
),

#Plaats 25
'erik-maes': Person(
    25,
    'Eric Maes',
    'Scheepvaartstraat 6 in <strong>Stevensvennen</strong>',
    49,
    'Gehuwd met Elly Bogaerts. Vader van Nathalie en Ellen',
    'Arbeider bij Sibelco',

    "<li>Nieuw</li>",

    "<li>Voorzitter van voetbalploeg FC Motorclub</li>"
    "<li>Voetbal en jagen zijn zijn passies</li>",

    'Wijkleven, Sport, Veiligheid, Sociale Zaken',
    'Zijn dochter Ellen baat een kinderopvang uit in Stevensvennen',
    'http://www.youtube.com/watch?v=s2tGPoG8LVg',
    "Belgium vs USSR - Mexico 1986",
    None,
    None,
    None,
    True,
    "Rasechte Lommelaar, man van het volk",
    "http://www.youtube.com/embed/fN2rv_aamEc",
    "M",
),

#Plaats 26
'veerle-baert': Person(
    26,
    'Veerle Baert',
    'Zwanenstraat 20 in Lommel <strong>Kolonie</strong>',
    40,
    'Gehuwd met Tom de Kort en mama van Elke (19), Shanti (16) en Lara (15)',
    'Loketbediende bij De Voorzorg in Lommel',

    "<li>Nieuw</li>",

    "<li>Soprtwedstrijden van de kinderen gaan bekijken</li>"
    "<li>Fietsen met de koersfiets</li>",

    'Sociale Zaken en Welzijn',
    'sportieve kinderen: Elke geeft tennisles, Lara is judoka en Shanti tennist',
    'http://www.youtube.com/watch?v=c8SL8vPr3a8',
    "Talent uit eigen tent (A. Delamazuretrio)",
    None,
    None,
    None,
    True,
    "Uw zorgen zijn mijn zorgen",
    "http://www.youtube.com/embed/4IiiJXYIFns",
    "F",
),

#Plaats 27
'sally-de-jong': Person(
    27,
    'Sally De jong',
    'Vreyshorring 194 in <strong>Centrum</strong>',
    31,
    'vrijgezel',
    'Verpleegkundige',

    "<li>Nieuw</li>",

    "<li>Sally is lid van de Neerpeltse tennisclub en speelt ook badminton</li>"
    "<li>Ze houdt van terrasjes, uit eten gaan met vrienden en familie</li>",

    'Sport, gezondheid en welzijn.',
    'Sally haar grootste schat heet "Einstein" en is een mini maltezer.',
    'http://www.youtube.com/watch?v=dnp2gHMecEU',
    "Najib Amhali",
    None,
    "http://www.facebook.com/sally.dejong1",
    None,
    True,
    "Met passie zorgen voor mensen",
    "http://www.youtube.com/embed/jyvkrCMJKkE",
    "F",
),

#Plaats 28
'ronny-geysen': Person(
    28,
    'Ronny Geysen',
    'Sparstraat 12, <strong>Heide-Heuvel</strong>',
    49,
    'Ongehuwd',
    'Bediende bij Philips Turnhout',

    "<li>6 jaar gemeenteraadslid</li>",

    "<li>Mountainbike bij Bike Action Team Lommel</li>"
    "<li>Bestuurslid bij supportersclub Heuvelhof, zijn hart klopt groen en wit</li>"
    "<li>Houdt van het Lommelse karnaval</li>"
    "<li>Citytrips</li>",

    'Milieu, Sport, Ruimtelijk Ordening, Lommel Leeft',
    'Ronny is de huidige voorzitter van de Sportraad',
    'http://www.youtube.com/watch?v=l457Eg33qJ4&feature=fvwrel',
    "Lassie",
    None,
    "http://www.facebook.com/ronnygeysen",
    None,
    True,
    "Een ambassadeur onder de mensen",
    "http://www.youtube.com/embed/F-BcU45SEq8",
    "M",
),

#plaats 29
'danny-huijsmans': Person(
    29,
    'Danny Huijsmans',
    'Kanaalstraat 19, <strong>Kerkhoven</strong>',
    57,
    'Gehuwd met Martien De Vrieze. Vader van Katelijne en Maarten',
    'Directeur Basisschool Sint-Jan Kerkhoven. Lid van het DB van de Directiecommissie Kath. Onderwijs',

    "<li>Nieuw</li>",

    "<li>Voorzitter bij muziekateliers Lommel</li>"
    "<li>Skiën en films kijken</li>"
    "<li>Supporter van Johan Vansummeren en Lommel United</li>"
    "<li>Lid van de Ervaringsgerichte contactgroep Limburg</li>",

    'Democratie, Verkeer, Cultuur, Sociale Zaken, Onderwijs',
    'Danny gaat al jaren mee tappen op Pukkelpop met de vereniging Lommel Rockt!',
    '',
    None,
    'huijsmansdanny',
    'https://www.facebook.com/huijsmansdanny',
    'http://www.sintjan-lommel.be',
    True,
    "Ik Lommel graag!",
    "http://www.youtube.com/embed/OfmMFtau6eU",
    "M",
),

#Plaats 30,
'fons-haagdoren': Person(
    30,
    'Fons Haagdoren',
    'Stortstraat 16 in <strong>Lommel-Barrier</strong>',
    69,
    'Gehuwd met Christiane Swerts. Heeft 1 zoon Philip (trainer Lommel United',
    'Pensioen',

    "<li>18 jaar Gemeenteraadslid waarvan 13 jaar als Schepen</li>",

    "<li>Tuinieren, sporten en sport kijken</li>"
    "<li>Organiseren van sportevenementen in de stad Lommel (profronde, superprestige Biljart, ...)</li>",

    'Sport, senioren',
    'Fons haalde ooit een cap als Rode Duivel',
    'http://www.youtube.com/watch?v=i48FDeuQCNI',
    "Profronde Lommel V03",
    None,
    None,
    None,
    True,
    "Mijn sport, mijn stad, mijn ervaring.",
    "http://www.youtube.com/embed/2pR8jWM1a1s",
    "M",
),

#Plaats 31
'francois-timmermans': Person(
    31,
    'Francois Timmermans',
    'Kloostersstraat 216 in <strong>Lutlommel</strong>',
    64,
    'Gehuwd met Thea',
    'Bruggepensioneerde',

    "<li>24 jaar Gemeenteraadslid waarvan 14 jaar als Schepen en OCMW-voorzitter</li>",

    "<li>Echte voetballiefhebber</li>"
    "<li>Voorzitter voetbalclub FC Germinal</li>"
    "<li>Penningmeester Verenigde LutlommelarenActief in de buurtwerking</li>",

    'Sport - Senioren - Sociale Zaken',
    'Francois werkte liefst 35 jaar bij De Voorzorg',
    'http://www.youtube.com/watch?v=uw-QCLbSedQ',
    "Hades - Lutlommel VV 1-5",
    None,
    None,
    None,
    True,
    "Een sociale aanpak loont",
    "http://www.youtube.com/embed/eVsm80mfCQo",
    "M",
)}




# Quick hack to have them as a sorted list, its a list of tuples (key,value)

#sorted(d.items(), key=itemgetter(1))
#input.sort(lambda x,y : cmp(x['name'], y['name']))
#sorted_persons = sorted(persons.items(), key=itemgetter(0))
persons_sorted = sorted(persons.items(), key=lambda (k, v): float(v.place))

