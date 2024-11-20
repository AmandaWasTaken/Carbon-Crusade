# Tänne tulee tietokantoihin liittyvät funktiot
# Voitte import databases as db nii ei tarvi kirjottaa niin paljoo

import mysql.connector

conn = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='projekti',
    user='root',
    password="Salasana123",
    autocommit=True,
)
'''
def fetch_airport_info(icao) -> None:

    sql = (f'SELECT local_code, municipality '
           f'FROM airport '
           f'WHERE ident="{icao}"')
    index = conn.cursor()
    index.execute(sql)
    res = index.fetchall()
    if index.rowcount > 0:
        for line in res:
            print(f"{line}")
Tää funktio on tarpeeton rn mut pidän varmuuden vuoks 
''' 

