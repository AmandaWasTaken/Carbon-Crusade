import random

import airportlogic
import gameplay

def fiftyfifty(country_options, correct_answer):
    incorrect_countries = []
    remaining_incorrect_country = random.randint(0, len(country_options) - 2)
    remaining_countries = []

    for country in country_options:
        if country != correct_answer:
            incorrect_countries.append(country)
        if country == correct_answer:
            remaining_countries.append(country)
    for i in range(0,len(incorrect_countries)):
        if i == remaining_incorrect_country:
            remaining_countries.append(incorrect_countries[i])
    return remaining_countries




if __name__ == "__main__":
    countries = ["suomi","ruotsi","viro","saksa"]
    correct_country = random.choice(countries)

    print(countries)
    print(fiftyfifty(countries, correct_country))
    print(correct_country)