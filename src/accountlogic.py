### TODO    fix create_account()
###         SQL queryssä tai db:ssä vika
###         finish login()

###         Jos haluutte testailla näitä nii lisätkää vaikka tän filun 
###         pohjaan ku näitä ei viel kutsuta missään

import databases as db
import re
cursor  = db.conn.cursor()

# Funktio hoitaa uuden käyttäjätilin luonnin ja lisäämisen tietokantaan
def create_account():

    while True:
        new_username = input("New Username: ")
        if len(new_username) <= 2:
            print("Username must be at least 3 characters long! ")
            continue
        else: break

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
        else: break

    table   = "game"
    last_id = "SELECT LAST_INSERT_ID()"
    cursor.execute(last_id)
    res = cursor.fetchall()[0][0]
    sql = (f'INSERT INTO {table} (screen_name, password) VALUES '
           f'({new_username}, {new_password}) WHERE id={res}')

    cursor.execute(sql)
    res = cursor.fetchall()
    for line in res:
        print(line)


# Funktio hoitaa käyttäjän sisäänkirjautumisen
def login():

    username = input("Input your username: ")

    username_check  = f'SELECT * FROM game WHERE screen_name="{username}"'

    cursor.execute(username_check)
    res = cursor.fetchall()
    if not res:
        print(f"Login Failed! (Username not found) ")
        exit(4)


    password = input("Input your password: ")
    pw_check = (f'SELECT * FROM game WHERE password="{password}" AND '
                f'screen_name="{username}"')
    cursor.execute(pw_check)
    res = cursor.fetchall()
    if not res:
        print("Login Failed! (Wrong password) ")
        exit(5)
    else:
        print(f"Welcome, {username}")

login()







