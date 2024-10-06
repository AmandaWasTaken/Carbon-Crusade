

import random
import databases
from geopy.distance import great_circle

# Hakee lentokentän ja koordinaatit, josta pelaaja lähtee liikkelle. 
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

# Tällä lasketaan etäisyys lähtöpisteen ja muiden pisteiden välillä.
def distance(startPoint, destPoint):
    
    dist = great_circle(startPoint, destPoint).kilometers
    return dist

# Hakee 30 lentokenttää, joista valitaan 5 arvauksia varten. Kaksi valitaan lähimmistä viidestä ja loput jäljellä olevasta listasta. Tehdään näistä vielä 
# listat, joissa maiden nimet, koordinaatit ja etäisyys lähtöpisteestä.  
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

    # Lista, jossa maat, koordinaatit ja etäisyys alkupisteeseen.
    distances = []
    for country in countries:
        countryName = country[0]
        coords = (country[1], country[2])
        dist = distance(startPoint, coords)
        distances.append((countryName, coords, dist))


    # Järjestetään etäisyyksien mukaan ja valitaan lähimmästä viidestä 2
    closestCountries = sorted(distances, key=lambda x: x[2])[:5]
    selectedClosest = random.sample(closestCountries, 2)

    # Lista jäljellä olevista maista poissulkien lähimmät valitut.
    remainingCountries = []
    for country in distances:
        if country not in selectedClosest:
            remainingCountries.append(country)


    selectedRemaining = random.sample(remainingCountries, 3)
    finalSelection = selectedClosest + selectedRemaining # Lopullinen lista maista

    return finalSelection, distances







