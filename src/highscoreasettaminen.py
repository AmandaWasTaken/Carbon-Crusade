import databases as db

def get_user_info (user):
    if db.conn.is_connected():
        cursor = db.conn.cursor()
        cursor.execute("""
        select game.id, goal.id
        from game
        inner join score on game.id = game_id
        inner join goal on goal.id = goal_id
        where screen_name = %s
        """, (user,))
        results = cursor.fetchall()
        return results[0]

def set_highscore(game_id, goal_id, user_score, user_name):
    try:
        if db.conn.is_connected():
            cursor = db.conn.cursor()
            cursor.execute("""
            update game
            set co2_consumed = %s
            where screen_name = %s
            """, (user_score,user_name))

        if db.conn.is_connected():
            cursor = db.conn.cursor()
            cursor.execute("""
                SELECT co2_consumed
                FROM game
                WHERE id = %s
            """, (game_id,))
            game_result = cursor.fetchone()

            if game_result:
                co2_consumed = game_result[0]
                if co2_consumed is None:
                    print(f"co2_consumed is NULL for game {game_id}")
                    return

                cursor.execute("""
                    SELECT highscore 
                    FROM goal
                    WHERE id = %s
                """, (goal_id,))
                goal_result = cursor.fetchone()

                if goal_result:
                    current_highscore = goal_result[0]

                    if current_highscore is None:
                        current_highscore = 0

                    co2_consumed = float(co2_consumed)
                    current_highscore = float(current_highscore)

                    if co2_consumed > current_highscore:
                        cursor.execute("""
                            UPDATE goal
                            SET highscore = %s
                            WHERE id = %s
                        """, (co2_consumed, goal_id))
                        db.conn.commit()
                        # print(f"High score päivitetty id:lle {goal_id} perustuen id:n {game_id} co2_consumediin")
                        print(f"Sait uuden highscoren pisteillä {user_score:,.0f} !")
                    else:
                        # print(f"co2_consumed ei ole korkeampi kuin tämän hetkinen high score id:lla {goal_id}")
                        print(f"Et saanut uutta highscorea.")

                else:
                    print(f"Ei highscore id:lla {goal_id}")
            else:
                print(f"Ei käyttäjää id:lla {game_id}")
    finally:
        if db.conn.is_connected():
            # cursor.close()
            # db.conn.close()
            pass
