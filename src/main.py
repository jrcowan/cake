from datetime import date

menu_options = {
    1: "Remember a new birthday.",
    2: "Tell me what birthdays you are tracking.",
    3: "Make changes to a birthday.",
    4: "Forget a birthday.",
    5: "Go away"
}


def print_menu():
    print("Is there something you would like for me to do?")
    print("\n")
    for key in menu_options.keys():
        print(key, ': ', menu_options[key])
    print("\n")


def create_birthday():
    while True:
        try:
            print("When is the birthday? [dd/mm/yyyy]")
            birthday = input().split('/')
            birthday = date(int(birthday[2]), int(birthday[1]), int(birthday[0]))
        except (ValueError, IndexError, OverflowError):
            print("Input was not recognized.")
            continue
        else:
            print(f"You said {birthday.day}/{birthday.month}/{birthday.year}. Is that correct?")
            answer = input().lower()
            if answer == "yes":
                print("Understood! I will remember this for you.")
                return birthday


def list_birthdays():  # TODO: create list_birthdays
    return any


def update_birthday():  # TODO: create update_birthday
    return any


def delete_birthday():  # TODO: create delete_birthday
    return any


if __name__ == '__main__':
    print("\n")
    print("Welcome to cake, the tool that reminds you of birthdays that you have a tendency to forget about.")
    while True:
        print_menu()
        option = int(input('Enter your choice: '))

        if option == 1:
            birthday = create_birthday()
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
