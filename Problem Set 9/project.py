import sqlite3

#import tkinter

def create_db_connection(name):
    connection = None

    try:
        connection = sqlite3.connect(name)
        return connection
    except sqlite3.Error as e:
        print(e)

def create_db_tables(connection, create_db_statement):
    cursor = connection.cursor()
    cursor.execute(create_db_statement)


def add_user(connection, name, balance, income):
    ...

def edit_user(connection, name, balance, income):
    # find user by id, change only what was passed - maybe use a dict
    ...

def add_expense(connection, title, exp_type, amount, recurring):
    ...

def edit_expense(connection, title, exp_type, amount, recurring):
    # same comment as edit_user function
    ...

def main():
    user_table = """CREATE TABLE IF NOT EXISTS user(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            balance FLOAT,
            income FLOAT,
            );"""

    expenses_table = """CREATE TABLE IF NOT EXISTS expenses(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            tite TEXT,
            type TEXT,
            amount FLOAT,
            recurring BOOLEAN,
            FOREIGN KEY(user_id) REFERENCES user_table(id)
            );"""

    connection = create_db_connection("Guac/Database/app.db")

    if connection is not None:
        create_db_tables(connection, user_table)
        create_db_tables(connection, expenses_table)
    else:
        print("Error cannot create connection to database")

