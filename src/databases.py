# Tänne tulee tietokantoihin liittyvät funktiot
import mysql.connector

conn = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='Salasana123',
    autocommit=True,
)

def foo() -> None:
    print("Moi")


