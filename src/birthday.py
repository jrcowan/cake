from datetime import date


def create_birthday():

    while True:
        birthday = get_birthday_value()
        confirmed = confirm_birthday_value(birthday)
        if confirmed:
            break


def get_birthday_value():
    try:
        print("When is the birthday? [dd/mm/yyyy]")
        birthday = input().split('/')
        birthday = date(int(birthday[2]), int(birthday[1]), int(birthday[0]))
        return birthday
    except (ValueError, IndexError, OverflowError):
        print("Input was not recognized.")


def confirm_birthday_value(birthday):
    print(f"You said {birthday.day}/{birthday.month}/{birthday.year}. Is that correct?")
    answer = input().lower()
    if answer == "yes":
        print("Understood! I will remember this for you.")
        return True
    elif answer == "no":
        print("Oh sorry, let's try that again.")
        return False
    else:
        print("Uh, I didn't understand that. Let's try that again.")
        return False


def list_birthdays():  # TODO: create list_birthdays
    return any


def update_birthday():  # TODO: create update_birthday
    return any


def delete_birthday():  # TODO: create delete_birthday
    return any

