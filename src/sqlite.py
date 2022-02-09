import sqlite3
from sqlite3 import Error

create_birthdays_table_sql = '''CREATE TABLE IF NOT EXISTS birthdays (
                                       id integer PRIMARY KEY,
                                       name text,
                                       date datetime
                                   );'''

create_birthday_entry_sql = ''' INSERT INTO birthdays(name, date)
              VALUES(?, ?) '''

database = r"cake.sqlite"


def create_table():
    try:
        connection = sqlite3.connect(database)
        return connection
    except Error as e:
        print(e)
    if connection is not None:
        try:
            c = connection.cursor()
            c.execute(create_birthdays_table_sql)
            return connection
        except Error as e:
            print(e)


def submit_birthday(connection, birthday):
    cur = connection.cursor()
    cur.execute(create_birthday_entry_sql, birthday)
    connection.commit()
    return cur.lastrowid
