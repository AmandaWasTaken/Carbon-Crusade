import random
import time

import airportlogic
import randomevents

from flask import Flask, request, jsonify, render_template
import json


app = Flask(__name__)


@app.route('/')
def gameplay():
    return render_template('gameplay.html')

@app.route('/compare_answer', methods=['POST'])
def compare_answer():
    data = request.get_json()

    player_answer = data.get('player_answer') #int
    countries = data.get('country_options') #list
    correct_answer = data.get('correct_country') #str

    if countries[player_answer - 1] == correct_answer:
        return jsonify({
            'success': True,
        })
    else:
        return jsonify({
            'success': False,
        })


@app.route('/remove_random_answers', methods=['POST'])
def remove_random_answers():
    data = request.get_json()

    remaining_country_indexes = data.get('remaining_country_indexes')
    correct_country_index = data.get('correct_country_index')

    while True:
        selection = random.randint(1,6)
        if remaining_country_indexes[selection-1] != 0 and remaining_country_indexes[selection-1] != correct_country_index:
            remaining_country_indexes[selection-1] = 0
            break

    return jsonify({
        'remaining_indexes': remaining_country_indexes,
        'selection': selection
                   })

@app.route('/count_player_points', methods=['POST'])
def count_player_points():
    data = request.get_json()

    flight_destination = data.get('flight_destination')
    country_options = data.get('country_options')
    turns_left = data.get('turns_left')

    gained_score = country_options[flight_destination - 1][2] * 0.15 * 396
    gained_score, turns_left, did_event_happen, event_text = roll_random_event(gained_score, turns_left)

    return jsonify ({
        'gained_score': gained_score,
        'turns_left': turns_left,
        'did_event_happen': did_event_happen,
        'event_text': event_text
    })


def roll_random_event(score, turns):
    new_score = score
    new_turns = turns
    event_text = ""
    did_event_happen = False
    random_event_roll = random.randint(1, 100)
    if random_event_roll <= 25:
        pos_or_neg_choice = random.randint(1, 2)
        pos_or_neg = ("Positive", "Negative")
        new_score, new_turns, event_text = randomevents.create_random_event(pos_or_neg[pos_or_neg_choice - 1], score, turns)
        did_event_happen = True
    return new_score, new_turns, did_event_happen, event_text

#, methods=['POST']
@app.route('/get_new_countries')
def get_new_countries():
    current_country = airportlogic.randomAirport()

    wrong_countries = airportlogic.getGuesses(current_country[1], current_country[2])

    all_country_options = [current_country[1]]
    for country in wrong_countries[0]:
        all_country_options.append(country[0])
    random.shuffle(all_country_options)


    # return all_country_options, current_country, wrong_countries
    return jsonify({
        'all_country_options': all_country_options,
        'current_country': current_country,
        'wrong_countries': wrong_countries
    })



if __name__ == '__main__':
    app.run(use_reloader=True, debug=True, host='127.0.0.1', port=5000)
