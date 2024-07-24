import random

computer_number = random.randint(0, 100)

while True:
    print() 
    user_guess = int(input("Guess a number between 0 and 100: "))
    print()
    if user_guess == computer_number:
        print(" Congratulations! You guessed the correct number!")
        break

    elif user_guess < computer_number:
        print()
        print("The secret number is higher than that.")
        print()

    else:
        print()
        print("The secret number is lower than that.")
        print()
