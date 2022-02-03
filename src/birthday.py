from datetime import date


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

