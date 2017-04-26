import random


# TODO: Unique names, not empty
# TODO:add commands to game (add user, remove user, help)


def validate_number(string):
    try:
        int(string)
    except ValueError:
        return False


def greater_than_zero(string):
    if int(string) > 0:
        return True
    return False


def commands(command):
    pass


def text_prompt(text):
    pass


def number_prompt(number):
    pass


def add_user(**users):
    pass


def remove_user(user):
    pass


def help():
    print "This a help message. \n You can you such commands as: \n " \
          "/add <user_name> - this command will add user to your game. \n " \
          "/remove <user_name> - this command will remove user from playing. \n " \
          "help - this command will display current message."


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


def check_winner(user, user_number, reserved_number):
    if reserved_number == user_number:
        print (bcolors.BOLD + bcolors.UNDERLINE + str(user).capitalize() + " you won!" + bcolors.ENDC + '\n')
        return True
    elif user_number > reserved_number:
        print (str(
            user) + " your number is " + bcolors.BOLD + bcolors.UNDERLINE + "greater" + bcolors.ENDC + " than was guessed. Next try.")
    elif user_number < reserved_number:
        print (str(
            user) + " your number is " + bcolors.BOLD + bcolors.UNDERLINE + "less" + bcolors.ENDC + " than was guessed. Next try.")
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
            if validate_number(your_number) and greater_than_zero(your_number):
                return your_number
            else:
                print "You entered negative number. Game is only with positive. Try again."
        except ValueError:
            print "Sorry, you entered not a number. Please, try again."


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = bcolors.ENDC
    BOLD = bcolors.BOLD + bcolors.UNDERLINE
    UNDERLINE = '\033[4m'
