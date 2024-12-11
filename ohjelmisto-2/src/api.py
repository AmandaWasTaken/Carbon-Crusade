from flask import Flask, request, jsonify, render_template, url_for
import mysql.connector
import json
import re
import databases as db
import top5highscore
import random
import time
import airportlogic
import randomevents


app = Flask(__name__)

def check_reserved(value_to_check: str) -> bool:
    cursor = db.conn.cursor()

    sql = f'select * from game where screen_name="{value_to_check}"'
    cursor.execute(sql)
    res = cursor.fetchall()
    if not res:
        return False
    return True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_account', methods=['POST'])
def create_account():
    cursor = db.conn.cursor()

    data = request.get_json()
    new_username = data.get("username")
    new_password = data.get("password")

    if len(new_username) <= 2:
        return jsonify({
            'success': False,
            'message': 'username must be at least 3 characters'
        })

    if check_reserved(new_username):
        return jsonify({
            'success': False,
            'message': 'username already taken'
        })

    if len(new_password) < 6:
        return jsonify({
            'success': False,
            'message': 'password must be at least 6 characters'
        })

        # regex tarkistaa että salasanassa on numero ja iso kirjain ja ei sisällä välilyöntejä
    pattern = '^(?!.*\\s)(?=.*[A-Z])(?=.*\\d).+$'
    res = re.match(pattern, new_password)
    if not res:
        return jsonify({
            'success': False,
            'message': 'password must contain at least one uppercase and one lowercase'
        })

    try:
        sql = f'INSERT INTO game (screen_name, password) VALUES ("{new_username}", "{new_password}")'
        cursor.execute(sql)
        db.conn.commit()

        return jsonify({
            'success': True,
            'message': f'Account created! Welcome {new_username}',
            'username': new_username
        })
    finally:
        cursor.close()


@app.route('/login', methods=['POST'])
def login():
    cursor = db.conn.cursor()

    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    try:
        username_check = f'SELECT * FROM game WHERE screen_name="{username}"'
        cursor.execute(username_check)
        res = cursor.fetchall()

        if not res:
            return jsonify({
                'success': False,
                'message': 'Username not found'
            })

        pw_check = f'SELECT * FROM game WHERE password="{password}" AND screen_name="{username}"'
        cursor.execute(pw_check)
        res = cursor.fetchall()

        if not res:
            return jsonify({
                'success': False,
                'message': 'Invalid password'
            })

        return jsonify({
            'success': True,
            'message': f'Welcome back, {username}!',
            'username': username
        })
    finally:
        cursor.close()

@app.route('/main_menu')
def main_menu():
    return render_template('mainmenu_page.html')

@app.route('/get_high_scores')
def get_high_scores_route():
    cursor = db.conn.cursor()
    query = """
        SELECT game.screen_name, goal.id AS goal_id, goal.highscore
        FROM score
        INNER JOIN game ON game.id = score.game_id
        INNER JOIN goal ON goal.id = score.goal_id
        ORDER BY goal.highscore DESC
        LIMIT 5;
    """
    cursor.execute(query)
    results = cursor.fetchall()

    scores = [
        {
            'screen_name': row[0],
            'goal_id': row[1],
            'highscore': row[2]
        }
        for row in results
    ]
    return jsonify(scores)

#################################################################

@app.route('/play')
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
    wrong_countries = data.get('wrong_countries')
    turns_left = data.get('turns_left')

    country_name = country_options[flight_destination - 1]
    # gained_score = country_options[flight_destination - 1][2] * 0.15 * 396
    country_index = 0
    apumuuttuja = 0
    for i in wrong_countries:
        if country_name in i:
            country_index = apumuuttuja
            break
        apumuuttuja += 1
    gained_score = wrong_countries[country_index][2] * 0.15 * 396
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
    # return jsonify({
    #     'message': "hellou"
    # })


if __name__ == '__main__':
    app.run(use_reloader=True, debug=True, host='127.0.0.1', port=5000)
