"""
4 August, 2020
This file has the necessary functions for database-related tasks.

In order to play, khoshgoman_
"""

import mysql.connector


def check_id_pass(player_id, password):
    with mysql.connector.connect(
            host="localhost",
            user="root",
            password="*****",           # replace asterisks with your MySql host password
            database="sql_khoshgoman"   # name of the database on my system
    ) as connection:
        command = "SELECT * FROM players"
        cursor = connection.cursor()
        cursor.execute(command)
        for each in cursor:
            if each[0] == player_id and each[1] == password:
                return True


def sign_in():
    while True:
        player_id = input("ID: ")
        password = input("Password: ")
        if check_id_pass(player_id, password):
            return player_id
        message = input("Id and password are not a match.\n"
                        "Enter to try again or enter 'q' to quit: ")
        if message == 'q':
            return False


def check_id(player_id):
    with mysql.connector.connect(
            host="localhost",
            user="root",
            password="*****",           # replace asterisks with your MySql host password
            database="sql_khoshgoman"
    ) as connection:
        command = "SELECT player_id FROM players"
        cursor = connection.cursor()
        cursor.execute(command)
        for each in cursor:
            if each[0] == player_id:
                return True


def sign_up():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    while True:
        player_id = input("Enter your desired id: ")
        if not check_id(player_id) and len(player_id.split()) == 1:
            break
        print("This id is used by another player.")
    password = input("Enter your desired and safe password: ")
    with mysql.connector.connect(
            host="localhost",
            user="root",
            password="*****",           # replace asterisks with your MySql host password
            database="sql_khoshgoman"
    ) as connection:
        command = "INSERT INTO players VALUES(%s, %s, %s, %s, %s, %s, %s)"
        cursor = connection.cursor()
        cursor.execute(command,
                       (player_id, password,
                        first_name, last_name,
                        0, 0, 0))
        connection.commit()
    return player_id


def enter_scoreboard(player_id, guess_number):
    with mysql.connector.connect(
            host="localhost",
            user="root",
            password="*****",           # replace asterisks with your MySql host password
            database="sql_khoshgoman"
    ) as connection:
        command = "INSERT INTO games (player_id, guess_number) " \
                  "VALUES(%s, %s)"
        cursor = connection.cursor()
        cursor.execute(command,
                       (player_id, guess_number))
        connection.commit()



