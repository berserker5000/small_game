import random


def validate_number(string):
    try:
        int(string)
        if string >= 0:
            return True
    except ValueError:
        return False


def greater_than_zerro(string):
    if int(string) > 0:
        return True
    return False


def get_users():
    while True:
        try:
            user_name = []
            users_in_game = raw_input("Enter number of players: ")
            for i in range(0, int(users_in_game)):
                user = raw_input("Enter " + str(i + 1) + " user name: ")
                user_name.append(user)
            return user_name
        except ValueError:
            print "Value Error!"


def do_move(user):
    while True:
        try:
            your_number = int(raw_input(str(user) + " please enter your number: "))
            if validate_number(your_number) and greater_than_zerro(your_number):
                return your_number
            else:
                print "You entered negative number. Game is only with positive. Try again."
        except ValueError:
            print "Sorry, you entered not a number. Please, try again."


def check_winner(user, user_number, reserved_number):
    if reserved_number == user_number:
        print ('\033[1m' + str(user).capitalize() + '\033[0m' + " you won!")
        return True
    elif user_number > reserved_number:
        print (str(user) + " your number is " + '\033[1m' + "greater" + '\033[0m' + " than was guessed. Next try.")
    elif user_number < reserved_number:
        print (str(user) + " your number is " + '\033[1m' + "less" + '\033[0m' + " than was guessed. Next try.")

    return False


def do_exit():
    while True:
        answer = raw_input("Do you want to play again? (Y/n): ")
        if not answer or answer.lower() in ('y', 'yes'):
            return True
        elif answer.lower() in ('n', 'no'):
            return False
        else:
            print("Not a valid answer!")


def generate_number():
    rnd = random.randint(1, 100)
    computer_number = random.randint(1, rnd)
    return computer_number


def start_game(users):

    computer_number = generate_number()
    for i in range(0, 100):
        for user in users:
            if check_winner(user, do_move(user), computer_number):
                return True


def main():
    users = get_users()
    while True:
        start_game(users)
        if not do_exit():
            return False


if __name__ == '__main__':
    main()
    exit()
