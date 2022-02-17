from datetime import date


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
            birthday = input().split('/')
            birthday = date(int(birthday[2]), int(birthday[1]), int(birthday[0]))
            return birthday
        except (ValueError, IndexError, OverflowError):
            print("I'm confused! Let's try that again.")


def confirm(name, birthday):
    while True:
        print(f"You said {name}'s birthday is {birthday.day}/{birthday.month}/{birthday.year}. Is that correct?")
        answer = input().lower()

        if answer == "yes" or "yeah":
            print("Understood! I will remember this for you.")
            return True
        elif answer == "no":
            print("Oh sorry, let's try that again.")
            return False
        else:
            print("Uh, I didn't understand that. Let's try that again.")
