import random

if (__name__ == "__main__"):
    print("This is an interactive guessing game!\nYou have to enter a number between 1 and 99 to find out the secret number.\nType 'exit' to end the game. Good luck!\n")

    mistery_number = random.randint(1, 99)
    attempts = 1
    finish = False
    while (finish == False):
        num = input("What's your guess between 1 and 99?\n>>  ")
        if (num == "exit"):
            print("Goodbye!")
            finish = True
        elif (num.isdigit() == False):
            print("That's not a number.")
            attempts += 1
        elif (int(num) == mistery_number and int(num) == 42):
            print("The answer to the ultimate question of life, the universe and everything is 42.\nCongratulations! You got it on your first try!")
            finish = True
        elif (int(num) == mistery_number):
            print(f"You won in {attempts} attempts!")
            finish = True
        else:
            if (int(num) > mistery_number):
                print("Too high!")
            else:
                print("Too low!")
            attempts += 1
    exit(0)
