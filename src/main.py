from src.birthday import *
from src.sqlite import *

menu_options = {
    1: "Remember a new birthday.",
    2: "Tell me what birthdays you are tracking.",
    3: "Make changes to a birthday.",
    4: "Forget a birthday.",
    5: "Go away."
}

database = r"cake.db"


def print_menu():
    print("Is there something you would like for me to do?")
    print("\n")
    for key in menu_options.keys():
        print(key, ': ', menu_options[key])
    print("\n")


if __name__ == '__main__':
    print("\n")
    print("Welcome to cake, the tool that reminds you of birthdays that you have a tendency to forget about.")

    connection = create_connection(r'cake.sqlite')
    if connection is not None:
        create_table(connection, sql_create_birthdays_table)

    while True:
        print_menu()
        option = int(input('Enter your choice: '))

        if option == 1:
            birthday = create_birthday(connection)
        elif option == 2:
            list_birthdays()
        elif option == 3:
            update_birthday()
        elif option == 4:
            delete_birthday()
        elif option == 5:
            exit()
        else:
            print('I didn\'t understand that. Let\'s try this again.')

