import pytest
from project import create_db_connection, add_user, add_expense, create_db_tables


def main():
    test_db()


def test_db():
    conn = create_db_connection("test.db")

    assert conn is not None

    cur = conn.cursor()

    create_table_statement = """CREATE TABLE IF NOT EXISTS test(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            balance FLOAT,
            income FLOAT,
            income_freq VARCHAR(3)
            );"""

    create_db_tables(conn, create_table_statement) 
    # Errors because I hardcoded the table "user" into the sql statement!
    add_user(conn, {"name": "tester1", "balance": 15000, "income": 12500, "income_freq": "BW"})

    record_length = cur.execute("SELECT COUNT(*) FROM user")
    print(record_length)

    conn.close()



if __name__ == "__main__":
    main()
