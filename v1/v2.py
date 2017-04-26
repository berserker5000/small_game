import random

computer_number = random.randint(1, 10)

def validate_positive_number(number):
    if number > 0 and type(number) == int:
        return True
    return False

def get_users():
    user_name = []
    users_in_game = input("Enter number of players: ")
    for i in range(0, int(users_in_game)):
        user = raw_input("Enter " + str(i + 1) + " user name: ")
        user_name.append(user)
    return user_name


def do_move(user):
    try:
        your_number = int(raw_input(str(user) + " please enter your number: "))
        if your_number < 0:
            print "You entered negative number. Gane is only with positive. Try again."
            do_move(user)
        return your_number
    except ValueError:
        print "Sorry, you entered not a number. Please, try again."
        do_move(user)


def check_winner(user, user_number, reserved_number):
    if reserved_number == user_number:
        print ('\033[1m' + str(user).capitalize() + '\033[0m' + " you won!")
        exit()
    elif user_number > reserved_number:
        print (str(user) + " your number is "+'\033[1m'+"greater"+'\033[0m'+ " than was guessed. Next try.")
    elif user_number < reserved_number:
        print (str(user) + " your number is "+'\033[1m'+"less"+'\033[0m'+ " than was guessed. Next try.")


def start_game(users, computer_number):
    print "You will have " + str(len(users)*5) + " tries to won"
    for i in range(0,len(users)*5):
        for user in users:
            check_winner(user, do_move(user), computer_number)


players = get_users()
start_game(players, computer_number)