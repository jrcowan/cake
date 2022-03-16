from datetime import date
from src import main, sqlite

menu_options = {
    1: "Remember a new birthday.",
    2: "Tell me what birthdays you are tracking.",
    3: "Make changes to a birthday.",
    4: "Forget a birthday.",
    5: "Go away.",
}


def print_menu():
    print("Is there something you would like for me to do?")
    print("\n")
    for key in menu_options.keys():
        print(key, ": ", menu_options[key])
    print("\n")


def start_console(connection):
    print("\n")
    print(
        "Welcome to cake, the tool that reminds you of birthdays that you have a tendency to forget about."
    )

    while True:
        print_menu()
        option = int(input("Enter your choice: "))

        if option == 1:
            name, date = get_input_for_create()
            sqlite.create_birthday_entry(connection, (name, date))
        elif option == 2:
            main.list_birthdays()
        elif option == 3:
            main.update_birthday()
        elif option == 4:
            main.delete_birthday()
        elif option == 5:
            exit()
        else:
            print("I didn't understand that. Let's try this again.")

def get_input_for_create():
    while True:
        name = get_name()
        birthday = get_date()
        confirmed = confirm(name, birthday)
        if confirmed:
            return name, birthday


def get_name():
    print("Whose birthday will I be remembering?")
    name = input()
    return name


def get_date():
    while True:
        try:
            print("When is the birthday? [dd/mm/yyyy]")
            birthday = input().split("/")
            birthday = date(int(birthday[2]), int(birthday[1]), int(birthday[0]))
            return birthday
        except (ValueError, IndexError, OverflowError):
            print("I'm confused! Let's try that again.")


def confirm(name, birthday):
    while True:
        print(
            f"You said {name}'s birthday is {birthday.day}/{birthday.month}/{birthday.year}. Is that correct?"
        )
        answer = input().lower()

        if answer == "yes" or "yeah":
            print("Understood! I will remember this for you.")
            return True
        elif answer == "no":
            print("Oh sorry, let's try that again.")
            return False
        else:
            print("Uh, I didn't understand that. Let's try that again.")
