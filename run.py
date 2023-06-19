import os


def clear():
    """
    Clear function to clean-up the terminal so things don't get messy.
    """
    os.system("cls" if os.name == "nt" else "clear")


def try_again(): 
    """
    Asks the user if they want to try the game again.
    Sends them back to the start or closes the program.
    """
    while True:
        answer = input("Would you like to try again? (yes/no): ")
        if answer[0].lower().strip() == "y":
            intro()
            break
        elif answer[0].lower().strip() == "n":
            clear()
            print("Thanks for playing Killer Cats.")
            break
        else:
            clear()
            print(f"{answer} Is not valid, please choose again")


def step_one():
    """
    First step of the game from going down the correct path.
    """
    clear()
    print("You sprint back, away from the growling.")
    print("Stumbling through the forest, you find a small dirt path.")
    print("It leads left, and right.")
    while True:
        answer = input("Which way do you go? (left/right)")
        if answer[0].lower().strip() == "l":
            # intro()
            break
        elif answer[0].lower().strip() == "r":
            # clear()
            # print("Thanks for playing Killer Cats.")
            break
        else:
            clear()
            print(f"{answer} Is not valid, please choose again")


def intro():
    """
    Called to start the game, gives the first question.
    """
    clear()
    print("You wake up, surrounded by trees and very confused.")
    print('"How did I get here?"')
    print("Your head hurts, you're covered in scratches.")
    print("You hear growling in front of you. It almost seems... familiar.")
    print("But you can't quite remember what happened.")
    while True:
        print("Option #1: Creep towards the growling to investigate.")
        print("Option #2: Run away from the growling as fast as possible.")
        answer = input("Which option will you choose? (1/2): ")
        clear()

        if answer.strip() == "1":
            print("You creep towards the growling.")
            print("The thick vegetation prevents you from seeing very far ahead.")
            print("But you continue on,")
            print("...straight into an army of cats...")
            print("Your last moments are a flurry of fur and hissing.")
            print("You have failed.")
            try_again()
            break
        elif answer.strip() == "2":
            step_one()
            break
        else:
            clear()
            print(f"{answer} Is not valid, please choose again")


if __name__ == "__main__":
    clear()
    intro()
