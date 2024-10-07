import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='hctest2',
    user='root',
    password='k0ira'
)

def get_top_scores():
    try:
        cursor = connection.cursor()
        query = """
            SELECT game.screen_name, goal.id AS goal_id, goal.highscore
            FROM score
            INNER JOIN game ON game.id = score.game_id
            INNER JOIN goal ON goal.id = score.goal_id
            ORDER BY goal.highscore DESC
            LIMIT 5;
        """
        #print("Kysely:", query)  #testaamista varten

        cursor.execute(query)
        results = cursor.fetchall()

        if not results:
            print("Ei löytynyt scoreja")
        else:
            print("Top 5 Scoret:")
            for row in results:
                print(f"Pelaaja: {row[0]}, Goal ID: {row[1]}, High Score: {row[2]}")

    finally:
        cursor.close()
        connection.close()

get_top_scores()