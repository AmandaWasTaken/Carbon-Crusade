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
            tulostus1, tulostus2 = ("Pelaaja:","High Score:")
            sijoitus = 1
            print(f"{tulostus1:23s}{tulostus2}")
            for row in results:
                score = row[2][0:-2]
                print(f"{sijoitus}. {row[0]:20s}{score}")
                sijoitus += 1

    finally:
        # cursor.close()
        # databases.conn.close()
        pass

