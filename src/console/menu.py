from src.birthday import list_birthdays, update_birthday, delete_birthday
from src.console.create import get_input_for_create
from src.sqlite.create import submit_birthday

menu_options = {
    1: "Remember a new birthday.",
    2: "Tell me what birthdays you are tracking.",
    3: "Make changes to a birthday.",
    4: "Forget a birthday.",
    5: "Go away."
}


def print_menu():
    print("Is there something you would like for me to do?")
    print("\n")
    for key in menu_options.keys():
        print(key, ': ', menu_options[key])
    print("\n")


def start_console(connection):
    print("\n")
    print("Welcome to cake, the tool that reminds you of birthdays that you have a tendency to forget about.")

    while True:
        print_menu()
        option = int(input('Enter your choice: '))

        if option == 1:
            name, date = get_input_for_create()
            submit_birthday(connection, (name, date))
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
