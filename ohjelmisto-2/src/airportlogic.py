

import random
import databases
from geopy.distance import great_circle

# Hakee lentokentän ja koordinaatit, josta pelaaja lähtee liikkelle. 
def randomAirport():
    sql = """
    SELECT DISTINCT airport.name, country.name, latitude_deg, longitude_deg 
    FROM airport 
    JOIN country ON airport.iso_country = country.iso_country 
    WHERE airport.type LIKE 'large_airport%' 
    ORDER BY rand() 
    LIMIT 1"""

    cursor = databases.conn.cursor()
    cursor.execute(sql)
    randAirport = cursor.fetchall()

    if not randAirport:
        raise ValueError("No airport found")

    rand_airportName = randAirport[0][0]
    rand_countryName = randAirport[0][1]
    rand_startPoint = (randAirport[0][2], randAirport[0][3])

    return rand_airportName, rand_countryName, rand_startPoint

# Tällä lasketaan etäisyys lähtöpisteen ja muiden pisteiden välillä.
def distance(startPoint, destPoint):
    
    dist = great_circle(startPoint, destPoint).kilometers
    return dist

# Hakee 30 lentokenttää, joista valitaan 5 arvauksia varten. Kaksi valitaan lähimmistä viidestä ja loput jäljellä olevasta listasta. Tehdään näistä vielä 
# listat, joissa maiden nimet, koordinaatit ja etäisyys lähtöpisteestä.  
def getGuesses(exceptionCountry, startPoint):
    # Use parameterized query to prevent SQL injection
    sql = """
    SELECT DISTINCT country.name, latitude_deg, longitude_deg
    FROM country
    JOIN airport ON country.iso_country = airport.iso_country
    WHERE airport.type LIKE 'large_airport%' AND country.name != %s
    GROUP BY country.name
    ORDER BY rand()
    LIMIT 30
    """

    cursor = databases.conn.cursor()
    cursor.execute(sql, (exceptionCountry,))
    countries = cursor.fetchall()

    # Create distances list with set to ensure unique countries
    seen_countries = set()
    distances = []
    for country in countries:
        countryName = country[0]
        if countryName not in seen_countries:
            coords = (country[1], country[2])
            dist = distance(startPoint, coords)
            distances.append((countryName, coords, dist))
            seen_countries.add(countryName)

    # Ensure we have enough unique countries
    if len(distances) < 5:
        raise ValueError("Not enough unique countries found")

    # Get closest countries
    closestCountries = sorted(distances, key=lambda x: x[2])[:5]
    selectedClosest = random.sample(closestCountries, 2)

    # Get remaining countries, ensuring no duplicates
    remainingCountries = [country for country in distances
                          if country not in selectedClosest]

    selectedRemaining = random.sample(remainingCountries, 3)
    finalSelection = selectedClosest + selectedRemaining

    return finalSelection, distances






