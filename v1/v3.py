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
    try:
        user_name = []
        users_in_game = raw_input("Enter number of players: ")
        for i in range(0, int(users_in_game)):
            user = raw_input("Enter " + str(i + 1) + " user name: ")
            user_name.append(user)
        return user_name
    except ValueError:
        return get_users()


def do_move(user):
    try:
        your_number = int(raw_input(str(user) + " please enter your number: "))
        if your_number < 0:
            print "You entered negative number. Gane is only with positive. Try again."
            do_move(user)
        return your_number
    except ValueError:
        print "Sorry, you entered not a number. Please, try again."
        return do_move(user)


def check_winner(user, user_number, reserved_number):
    if validate_number(user_number):
        if reserved_number == user_number:
            print ('\033[1m' + str(user).capitalize() + '\033[0m' + " you won!")
            do_exit()
        elif user_number > reserved_number:
            print (str(user) + " your number is " + '\033[1m' + "greater" + '\033[0m' + " than was guessed. Next try.")
        elif user_number < reserved_number:
            print (str(user) + " your number is " + '\033[1m' + "less" + '\033[0m' + " than was guessed. Next try.")
    else:
        print "Some shit happens. New try."
        return check_winner(user, user_number, reserved_number)


def do_exit():
    yes = ['y', 'yes', 'ye']
    no = ['n', 'no', 'ne']
    ex = raw_input("Do you want to exit game? \n")
    if ex.lower() in yes:
        print "Thanks for your play. Good bye!"
        exit()
    elif ex.lower() in no:
        return True
    else:
        print "I don't understand you.\n Enter a normal answer: yes or no."
        return True


def generate_number(users):
    len_users = len(users)
    rnd = random.randint(1, 10 ** len_users)
    computer_number = random.randint(1, rnd)
    return computer_number


def start_game(users, number):
    print "You will have " + str(len(users) * 5) + " tries to won"
    for i in range(0, len(users) * 5):
        for user in users:
            check_winner(user, do_move(user), number)


users = get_users()

start_game(users, generate_number(users))
