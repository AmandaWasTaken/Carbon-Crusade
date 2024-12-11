from flask import Flask, request, jsonify, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template('mainmenu_page.html')


@app.route('/api/game', methods=['POST'])
def handle_game_action():
    data = request.get_json()
    action = data.get('action')
    user = data.get('user')

    if action == 'start_game':
        difficulty = data.get('difficulty')
        score = startGameplayLoop(int(difficulty))
        return jsonify({
            'success': True,
            'score': score
        })

    elif action == 'get_highscores':
        scores = top5highscore.get_top_scores()
        return jsonify({
            'success': True,
            'scores': scores
        })

    elif action == 'get_credits':
        return jsonify({
            'success': True,
            'credits': CREDITS
        })


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response


if __name__ == '__main__':
    app.run(debug=True, port=5000)