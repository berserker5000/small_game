from libraries import generate_number, check_winner, do_move, get_users, do_exit, bcolors


def start_game(users):
    computer_number = generate_number()
    move = 0
    while True:
        for user in users:
            move +=1
            if check_winner(user, do_move(user), computer_number):
                print bcolors.BOLD + user + " won this game in "+ str(move) + " moves. Congratulates!" + bcolors.ENDC
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
