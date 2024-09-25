import random
import databases
from geopy.distance import great_circle

def randomAirport():

    sql = """
    SELECT airport.name, country.name, latitude_deg, longitude_deg 
    FROM airport 
    JOIN country ON airport.iso_country = country.iso_country 
    WHERE airport.type LIKE 'large_airport%' 
    ORDER BY rand() 
    LIMIT 1"""
    #Valitaan satunnainen lentokenttä ja maa, jossa lentokenttä sijaitsee

    cursor = databases.conn.cursor()
    cursor.execute(sql)

    #Halutaan ulos satunnaisen lentokentän nimi ja maa
    randAirport = cursor.fetchall()
    airportName = randAirport[0][0]
    countryName = randAirport[0][1]
    startPoint = (randAirport[0][2], randAirport[0][3])

    #print(airportName, countryName)
    return airportName, countryName, startPoint

def wrongCountry(exceptionCountry):

    sql = """
    SELECT DISTINCT country.name, latitude_deg, longitude_deg
    from country
    JOIN airport ON country.iso_country = airport.iso_country
    WHERE airport.type LIKE 'large_airport%' AND country.name != '{exceptionCountry}'
    ORDER BY rand()
    LIMIT 5
    """

    cursor = databases.conn.cursor()
    cursor.execute(sql)

    wrongCountries = cursor.fetchall()

    return [(country[0], country[1], country[2]) for country in wrongCountries]

def distance(startPoint, destPoint):

    alku = (startPoint)
    loppu = (destPoint)
    dist = great_circle(alku, loppu).kilometers

    return dist

airportName, countryName, startPoint = randomAirport()
wNamesAndCoords = wrongCountry(countryName)
wNames = [country[0] for country in wNamesAndCoords]

countryChoices = [countryName] + wNames
random.shuffle(countryChoices)

startLat, startLon = startPoint
print(f'Starting point: {countryName}, {airportName}, ({startLat}, {startLon})\n')

for country in wNamesAndCoords:
    destName = country[0]
    destPoint = (country[1], country[2])
    distancefrom = distance(startPoint, destPoint)
    print(f'Maassa {destName} sijaitsevan lentokentän etäisyys lähtöpisteestä on {distancefrom: .0f}km. Päätepisteen koordinaatit ovat {destPoint}. ')

print(f"\n{countryChoices}")



"""

Teeppä kommentit.
tehdä tapa että pelaaja voi valita noista vaihtoehdoista
muita juttuja en jake pohtia

seuraavaks pitää tehä logiikka et toi valitsee vääristä maista x määrän y etäisyyden päästä. 


jossai vaiheessa muuta randairport ja wrongcountries 1 funktioksi 
sen pitäisi valita yksi niistä olemaan aloitus paikka.
hmm
"""

