create_birthday_entry_sql = ''' INSERT INTO birthdays(name, date)
              VALUES(?, ?) '''


def submit_birthday(connection, birthday):
    cur = connection.cursor()
    cur.execute(create_birthday_entry_sql, birthday)
    connection.commit()
    return cur.lastrowid
