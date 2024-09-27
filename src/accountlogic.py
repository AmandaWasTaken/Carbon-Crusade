### TODO    fix create_account()
###         SQL queryssä tai db:ssä vika
###         finish login()

###         Jos haluutte testailla näitä nii lisätkää vaikka tän filun 
###         pohjaan ku näitä ei viel kutsuta missään

import databases as db
import re
cursor  = db.conn.cursor();

def create_account():

    new_username = input("New Username: ")
    if len(new_username) <= 2:
        print("Username must be at least 3 characters long! ")
        exit(1)
    
    new_password = input("New Password: ")
    if len(new_password) < 6:
        print("Password must be at least 6 charactes long! ")
        exit(2)
    
    # regex tarkistaa että salasanassa on numero ja iso kirjain
    pattern = r'(?=.*[A-Z])(?=.*\d)'    
    res = re.match(pattern, new_password) 
    if not res:
        print("Password must include at least one capital letter and a number! ")
        exit(3)

    print(f"New username: {new_username}, new password: {new_password}")
    table   = "game"
    last_id = "SELECT LAST_INSERT_ID()"
    cursor.execute(last_id)
    res = cursor.fetchall()
    res = res[0][0]
    sql = (f'INSERT INTO {table} (screen_name, password) VALUES '
           f'({new_username}, {new_password}) WHERE id={res+1}')

    cursor.execute(sql)
    res = cursor.fetchall()
    for line in res:
        print(line)
    print(sql)



def login():

    username = input("Input your username: ")
    password = input("Input your password: ")

    username_check  = (f'SELECT * FROM game WHERE screen_name="{username}"')
    pw_check        = (f'SELECT * FROM game WHERE password="{password}" AND '
                       f'screen_name="{username}"')

    cursor.execute(username_check)    
    res = cursor.fetchall()
    if not res:
        print(f"Login Failed! (Wrong username) ")
        exit(4)
    else:
        print(f"Welcome, {username}!")

    cursor.execute(pw_check)
    res = cursor.fetchall()
    if not res:
        print("Login Failed! (Wrong password) ")











