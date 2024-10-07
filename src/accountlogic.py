import databases as db
import re
cursor = db.conn.cursor()

def check_reserved(value_to_check: str) -> bool:

    sql = f'select * from game where screen_name="{value_to_check}"'
    cursor.execute(sql)
    res = cursor.fetchall()
    if not res:
        return False 
    return True

# Funktio hoitaa uuden käyttäjätilin luonnin ja lisäämisen tietokantaan
def create_account():

    while True:
        new_username = input("New Username: ")
        if len(new_username) <= 2:
            print("Username must be at least 3 characters long! ")
            continue
        if check_reserved(new_username):
            print("Username Taken")
            continue
        break

    while True:
        new_password = input("New Password: ")
        if len(new_password) < 6:
            print("Password must be at least 6 charactes long! ")
            continue
    
        # regex tarkistaa että salasanassa on numero ja iso kirjain ja ei sisällä välilyöntejä
        pattern = '^(?!.*\\s)(?=.*[A-Z])(?=.*\\d).+$'
        res = re.match(pattern, new_password)
        if not res:
            print("Password must include at least one capital letter and a number and can't contain spaces! ")
            continue
        break

    table   = "game"
    sql = (f'INSERT INTO {table} (screen_name, password) VALUES ("{new_username}", "{new_password}")')

    cursor.execute(sql)
    res = cursor.fetchall()

# Funktio hoitaa käyttäjän sisäänkirjautumisen
def login():

    logged_in = False
    while True:
        username = input("Input your username: ")
        username_check  = f'SELECT * FROM game WHERE screen_name="{username}"'
        cursor.execute(username_check)
        res = cursor.fetchall()
        if not res:
            print(f"Login Failed! (Username not found) ")
            continue
        break

    while True:
        password = input("Input your password: ")
        pw_check = (f'SELECT * FROM game WHERE password="{password}" AND '
                f'screen_name="{username}"')
        cursor.execute(pw_check)
        res = cursor.fetchall()
        if not res:
            print("Login Failed! (Wrong password) ")
            continue

        logged_in = True
        print(f"Welcome, {username}")
        break
