import databases

def get_top_scores():
    try:
        cursor = databases.conn.cursor()
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
        databases.conn.close()

get_top_scores()