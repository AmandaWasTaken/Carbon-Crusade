import random
import time

import airportlogic
import randomevents2 as randomevents

def printCurrentAirport(airport_name):
    print(f"Olet tällä hetkellä lentokentällä {airport_name}. Missä maassa kyseinen lentokenttä sijaitsee?")
    return


def printCountryOptions(country_list):
    option = 0
    for country in country_list:
        print(f"{option + 1}. {country}")
        option += 1
    return


def printInstructions():
    print(f"-----------------------------------------------------------------------------------------------")
    print(f"--- Pelin tarkoituksena on kerätä mahdollisimman paljon co2-päästöjä 24kk aikana.           ---")
    print(f"--- Syötä vastauksesi kysymyksiin numeroin 1-6.                                             ---")
    print(f"--- Syötä 'ohjeet' jos haluat lukea ohjeet uudestaan tai 'exit' jos haluat poistua pelistä. ---")
    print(f"-----------------------------------------------------------------------------------------------\n")
    return


def askPlayerAnswer(country_options):
    while True:
        try:
            player_answer = input(f"Syötä vastauksesi numero: ")
            if player_answer == "ohjeet":
                printInstructions()
                printCountryOptions(country_options)
                continue
            if player_answer not in ("1", "2", "3", "4", "5", "6"):
                raise TypeError
            elif country_options[int(player_answer) - 1] == "-":
                raise ValueError
            return int(player_answer)
        except TypeError:
            print(f"\nSyötteesi oli virheellinen, anna uusi vastaus numeroista 1-6")
            printCountryOptions(country_options)
        except ValueError:
            print(f"\nSyötit poistetun vastauksen, anna uusi vastaus numeroista 1-6")
            printCountryOptions(country_options)


def comparePlayerAnswer(player_answer, countries, correct_answer):
    if countries[player_answer - 1] == correct_answer:
        return True
    else:
        return False


def removeWrongAnswers(country_options, wrong_countries, player_answer):
    new_country_list = []
    furthest_option = ""
    furthest_distance = 0

    for country in wrong_countries:
        if country[2] > furthest_distance and country[0] in country_options and country[0] != country_options[
            player_answer - 1]:
            furthest_distance = country[2]
            furthest_option = country[0]

    for country in country_options:
        if country != furthest_option and country != country_options[player_answer - 1]:
            new_country_list.append(country)
        else:
            new_country_list.append("-")

    return new_country_list


def playerGetsCorrectAnswer(current_country, remaining_countries, flight_options):
    remaining_countries[remaining_countries.index(current_country)] = "-"

    print(f"\nVastauksesi {current_country} on oikein!")
    print(
        "Seuraavaksi valitse jäljellä olevista vaihtoehdoista mihin maahan haluat lentää kerätäksesi mahdollisimman paljon co2-päästöjä.")
    printCountryOptions(remaining_countries)

    player_choice = askPlayerAnswer(remaining_countries)

    for i in flight_options:
        if i[0] == remaining_countries[player_choice - 1]:
            co2_emissions = i[2]
            player_choice_country = i[0]

    co2_emissions = co2_emissions * 0.15 * 396

    print(f"Päätit lentää maahan {player_choice_country}, joten sait kerrytettyä {co2_emissions:,.0f}kg co2-päästöjä.")
    return co2_emissions



def startGameplayLoop(difficulty):

    print(f"{difficulty}")

    game_running = True
    score = 0
    turns_left = 12
    difficulties = ("Helppo", "Normaali", "Vaikea")
    score_limits = (1000000, 2000000, 3000000)

    print(f"\nTervetuloa Carbon Crusade:n pariin! Valitsemasi vaikeustaso on {difficulties[difficulty - 1]}, ")
    print(f"joten sinun täytyy kerätä {score_limits[difficulty - 1]:,.0f}kg co2-päästöjä päästäksesi pelin läpi.\n")
    time.sleep(3)
    printInstructions()
    time.sleep(3)

    while game_running and turns_left > 0:
        print(f"\nOlet aiheuttanut {score:,.0f}kg co2-päästöjä, kun sinulla on jäljellä {turns_left}kk aikaa.\n")

        current_country = airportlogic.randomAirport()

        wrong_countries = airportlogic.getGuesses(current_country[1], current_country[2])

        all_country_options = [current_country[1]]
        for country in wrong_countries[0]:
            all_country_options.append(country[0])
        random.shuffle(all_country_options)

        for attempt in range(1, 4):
            printCurrentAirport(current_country[0])
            printCountryOptions(all_country_options)

            player_answer = askPlayerAnswer(all_country_options)
            comparison = comparePlayerAnswer(player_answer, all_country_options, current_country[1])
            if comparison:
                gained_score = playerGetsCorrectAnswer(current_country[1], all_country_options, wrong_countries[0])
                roll_random_event = random.randint(1,100)
                if roll_random_event <= 25:
                    pos_or_neg_choice = random.randint(1,2)
                    pos_or_neg = ("Positive","Negative")
                    gained_score = randomevents.create_random_event(pos_or_neg[pos_or_neg_choice-1], gained_score)
                score += gained_score
                turns_left -= 1
                break
            elif attempt < 3:
                print(
                    f"\nVastauksesi on valitettavasti väärin. Sinulla on yrityksiä tälle kysymykselle jäljellä {3 - attempt} kpl.")
                all_country_options = removeWrongAnswers(all_country_options, wrong_countries[0], player_answer)
            else:
                print(f"\nVastauksesi on valitettavasti väärin. Oikea vastaus on {current_country[1]}.")
                print("Et valitettavasti saanut kerrytettyä yhtään co2-päästöjä tässä kuussa.")
                turns_left -= 1
    print(f"Kiitos Carbon Crusaden pelaamisesta! Sait kerättyä itsellesi {score:,.0f}kg verran co2-päästöjä!")
    return (score, difficulty)

#startGameplayLoop(1)