from libraries import generate_number, bcolors, number_prompt


def check_winner(user, user_number, reserved_number):
    if reserved_number == user_number:
        print (bcolors.BOLD + str(user).capitalize() + " you won!" + bcolors.ENDC + '\n')
        return True
    elif user_number > reserved_number:
        print (str(
            user) + " your number is " + bcolors.BOLD + "greater" + bcolors.ENDC + " than was guessed. Next try.")
    elif user_number < reserved_number:
        print (str(
            user) + " your number is " + bcolors.BOLD + "less" + bcolors.ENDC + " than was guessed. Next try.")
    return False


def get_users():
    # n = ask_number("Get me number: ", min, max)
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
            if validate_number(your_number):
                return your_number
            else:
                print "You entered negative number. Game is only with positive. Try again."
        except ValueError:
            print "Sorry, you entered not a number. Please, try again."


def do_exit():
    while True:
        answer = raw_input("Do you want to play again? (Y/n): ")
        if not answer or answer.lower() in ('y', 'yes'):
            return True
        elif answer.lower() in ('n', 'no'):
            return False
        else:
            print("Not a valid answer!")


def start_game(users):
    computer_number = generate_number()
    move = 0
    while True:
        for user in users:
            move += 1
            if check_winner(user, do_move(user), computer_number):
                print bcolors.BOLD + user + " won this game in " + str(move) + " moves. Congratulates!" + bcolors.ENDC
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
