from datetime import date


if __name__ == '__main__':
    print("\n\nWelcome to cake, the tool that reminds you of birthdays that you have a tendency to forget about.\n")
    while True:
        try:
            print("Please enter your birthday in dd/mm/yyyy format.")
            birthday = input().split('/')
            birthday = date(int(birthday[2]), int(birthday[1]), int(birthday[0]))
        except (ValueError, IndexError, OverflowError):
            print("Input was not recognized.")
            continue
        else:
            print(f"Your entry was {birthday.day}/{birthday.month}/{birthday.year}. Is that correct?")
            answer = input().lower()
            if answer == "yes":
                break



