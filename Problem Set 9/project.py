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


def add_user(connection, data):
    # data = { "name": "user1", "balance": 15000, "income": 7500, "income_freq": "BW" }
    cursor = connection.cursor()
    cursor.executemany("""INSERT INTO user VALUES(:name, :balance, :income, :income_freq)""", data)

def edit_user(connection, id, data):
    # find user by id, change only what was passed - maybe use a dict
    ...

def add_expense(connection, id, data):
    cursor = connection.cursor()
    cursor.executemany("INSERT INTO expenses VALUES(:title, :type, :amount, :expense_freq)", data)

def edit_expense(connection, title, exp_type, amount, recurring):
    # same comment as edit_user function
    ...

def main():
    user_table = """CREATE TABLE IF NOT EXISTS user(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            balance FLOAT,
            income FLOAT,
            income_freq VARCHAR(3),
            );"""

    expenses_table = """CREATE TABLE IF NOT EXISTS expenses(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            title TEXT,
            type TEXT,
            amount FLOAT,
            expense_freq VARCHAR(3)
            FOREIGN KEY(user_id) REFERENCES user(id)
            );"""

    connection = create_db_connection("app.db")

    if connection is not None:
        create_db_tables(connection, user_table)
        create_db_tables(connection, expenses_table)
    else:
        print("Error cannot create connection to database")

#add user

