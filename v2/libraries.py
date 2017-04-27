import random


# TODO: Unique names, not empty
# TODO:add commands to game (add user, remove user, help)


def validate_number(string):
    try:
        int(string)
        if int(string) > 0:
            return True
    except ValueError:
        return False


def commands(command):
    pass


def text_prompt(text):
    pass


def number_prompt(ask, **minimum, **maximum):
    while True:
        prompt = raw_input(ask)
        if validate_number(prompt):
            if prompt>minimum and prompt<maximum:
                return prompt



def add_user(**users):
    pass


def remove_user(user):
    pass


def help():
    return "This a help message. \n You can you such commands as: \n " \
          "/add <user_name> - this command will add user to your game. \n " \
          "/remove <user_name> - this command will remove user from playing. \n " \
          "help - this command will display current message."





def generate_number():
    #rnd = random.randint(1, 100)
    computer_number = random.randint(1, 100)
    return computer_number





class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
