import random
computer_number = random.randint(0,100)
while True:
    your_number = input("Enter your number: ")
    if computer_number == your_number:
        print ("You won!")
    else:
        if your_number>computer_number:
            print ("Your number is greater than was guessed. Next try.")
        elif your_number<computer_number:
            print ("Your number is less than was guessed. Next try.")