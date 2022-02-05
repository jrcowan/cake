import sqlite3
from sqlite3 import Error

from src import birthday

sql_create_birthdays_table = """ CREATE TABLE IF NOT EXISTS birthdays (
                                       id integer PRIMARY KEY,
                                       name text,
                                       date datetime
                                   ); """


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)

    return connection


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def submit_birthday(connection, name, date):
    """
    Submit a new birthday into the birthdays table
    :param connection:
    :param birthday:
    :return: birthday id
    """
    sql = ''' INSERT INTO birthdays(name, date)
              VALUES(?, ?) '''
    cur = connection.cursor()
    birthday = (name, date)
    cur.execute(sql, birthday)
    connection.commit()
    return cur.lastrowid
