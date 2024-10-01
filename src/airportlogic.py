### TODO
### mahdollisesti koita grind getGuesses hakemaan n määrä maita
###
### kommentit
### yksi lista josta tehdä toi arvaus
### eli randAp + selectedCountries



import random
import databases
from geopy.distance import great_circle

# Haistappa juho kukka
def randomAirport():

    sql = """
    SELECT airport.name, country.name, latitude_deg, longitude_deg 
    FROM airport 
    JOIN country ON airport.iso_country = country.iso_country 
    WHERE airport.type LIKE 'large_airport%' 
    ORDER BY rand() 
    LIMIT 1"""
    # Haetaan lentokenttä, maa(jossa ap on) ja koordinaatit.

    cursor = databases.conn.cursor()
    cursor.execute(sql)
    randAirport = cursor.fetchall()
    rand_airportName = randAirport[0][0]
    rand_countryName = randAirport[0][1]
    rand_startPoint = (randAirport[0][2], randAirport[0][3])
    # Tehdään sql-haulla saaduista tiedoista lista randAirport ja siirretään tiedot käyttöä varten jokaisesta sarakkeesta omaan muuttujaan.
    # Sanakirja voisi toimia yleisemmin, mutta toisessa funktiossa se olisi turhan monimutkaista.

    return rand_airportName, rand_countryName, rand_startPoint

def distance(startPoint, destPoint):
    #Tällä lasketaan etäisyys lähtömaan ja muiden maiden välillä.
    dist = great_circle(startPoint, destPoint).kilometers
    return dist

def getGuesses(exceptionCountry, startPoint):

    sql = """
    SELECT country.name, latitude_deg, longitude_deg
    from country
    JOIN airport ON country.iso_country = airport.iso_country
    WHERE airport.type LIKE 'large_airport%' AND country.name != '{exceptionCountry}'
    GROUP BY country.name
    ORDER BY rand()
    LIMIT 30
    """
    # Haetaan 30 maata, joissa "large_airport" ja lentokenttien koordinaatit

    cursor = databases.conn.cursor()
    cursor.execute(sql)
    countries = cursor.fetchall()
    # Tehdään lista sql-haulla saaduista tiedoista.

    # Lista, jossa maat, koordinaatit ja etäisyys alkupisteeseen.
    distances = []
    for country in countries:
        countryName = country[0]
        coords = (country[1], country[2])
        dist = distance(startPoint, coords)
        distances.append((countryName, coords, dist))
    #List comprehension??

    #print(distances)

    # Järjestetään etäisyyksien mukaan ja valitaan lähimmästä viidestä 2
    closestCountries = sorted(distances, key=lambda x: x[2])[:5]
    selectedClosest = random.sample(closestCountries, 2)

    # Lista jäljellä olevista maista poissulkien lähimmät valitut.
    remainingCountries = []
    for country in distances:
        if country not in selectedClosest:
            remainingCountries.append(country)
    # List comprehension when??

    #
    # ^^ vois vaa valita distances listasta ja laittaa exclude
    # maat jotka on selectedClosest ??
    #
    #


    selectedRemaining = random.sample(remainingCountries, 3)
    finalSelection = selectedClosest + selectedRemaining # Lopullinen lista maista

    # Pitäiskö tää saada palauttaa se määrä maita jonka haluan?

    return finalSelection, distances


rand_airportName, rand_countryName, rand_startPoint = randomAirport()
selectedCountries, allCountries = getGuesses(rand_airportName, rand_startPoint)


selectedCountryNames = []
for country in selectedCountries:
    selectedCountryNames.append(country[0])
# list comprehension bruda

guesses = [rand_countryName] + selectedCountryNames
random.shuffle(guesses)
print(guesses)



# Alla koodin testailua varten
#
#
#
#
#

startLat, startLon = rand_startPoint
#print(f'Starting point: {rand_countryName}, {rand_airportName}, ({startLat}, {startLon})\n')




for country in selectedCountries:
    destName = country[0]
    destPoint = country[1]
    distanceFrom = country[2]
    #print(f'Maassa {destName} sijaitsevan lentokentän etäisyys lähtöpisteestä on {distanceFrom: .0f}km. Päätepisteen koordinaatit ovat {destPoint}. ')







