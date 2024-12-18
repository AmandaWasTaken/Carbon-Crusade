from flask import Flask, request, jsonify, render_template
import mysql.connector
import json
import re
import databases as db


app = Flask(__name__)

def check_reserved(value_to_check: str) -> bool:
    cursor = db.conn.cursor()

    sql = f'select * from game where screen_name="{value_to_check}"'
    cursor.execute(sql)
    res = cursor.fetchall()
    if not res:
        return False
    return True


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


if __name__ == '__main__':
    app.run(use_reloader=True, debug=True, host='127.0.0.1', port=5000)
