import random

# import airportlogic
# import gameplay

def fiftyfifty(country_options, correct_answer):
    incorrect_countries = []
    remaining_incorrect_country = []
    remaining_countries = []

    for country in country_options:
        if country != correct_answer:
            incorrect_countries.append(country)
        if country == correct_answer:
            remaining_countries.append(country)

    while len(remaining_incorrect_country) + 1 != int(len(countries) / 2):
        random_incorrect_country = random.choice(incorrect_countries)
        if random_incorrect_country not in remaining_incorrect_country:
            remaining_incorrect_country.append(random_incorrect_country)

    for country in remaining_incorrect_country:
        remaining_countries.append(country)

    return remaining_countries


if __name__ == "__main__":
    countries = ["suomi","ruotsi","viro","saksa","norja","tanska"]
    correct_country = random.choice(countries)

    print(countries)
    print(fiftyfifty(countries, correct_country))
    print(correct_country)