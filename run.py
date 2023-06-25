import os
import title

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
            print("Oh no, you let the cats win!\nThank you for playing Killer Cats.")
            break
        else:
            clear()
            print(f"{answer} Is not valid, please choose again.\n")


# def verification():
#     while True:
#         human_verification = input("Verify your humanity by typing 'human' here, no cats allowed!: ")
#         if human_verification[0].lower().strip() == "h":
#             intro()
#         elif human_verification[0].lower().strip() == "c":
#             clear()
#             print("NO CATS ALLOWED!\n")
#         else: 
#             clear()
#             print(f"{human_verification} Is not valid, please choose again.\n")


def welcome():
    """
    First thing displayed when the program is run.
    """
    clear()
    print(title.title)
    print("\nWelcome to Killer cats!\n")
    print("To embark on this journey through the apocalypse will be no easy feat.")
    print("At each step in your path, you will be faced with a choice.")
    print("This choice could lead to your death, or your salvation. So choose wisely.")
    print("Be warned: This world is run by intelligent cats equipped with opposable thumbs\nand ammunition. Keep your wits about you survivor, and don't let the cats win.\n")
    while True:
        human_verification = input("Verify your humanity by typing 'human' here, no cats allowed!: ")
        if human_verification[0].lower().strip() == "h":
            intro()
            break
        elif human_verification[0].lower().strip() == "c":
            clear()
            print("NO CATS ALLOWED!\n")
        else: 
            clear()
            print(f"{human_verification} Is not valid, please choose again.\n")


def intro():
    """
    Called to start the game, gives the first question.
    """
    clear()
    print("You wake up, surrounded by trees and very confused.")
    print('"How did I get here?"')
    print("Your head hurts, you're covered in scratches.")
    print("You hear growling in front of you. It almost seems... familiar.")
    print("But you can't quite remember what happened.\n")
    while True:
        print("Option #1: Creep towards the growling to investigate.")
        print("Option #2: Run away from the growling as fast as possible.\n")
        answer = input("Which option will you choose? (1/2): ")
        clear()

        if answer.strip() == "1":
            print("You creep towards the growling.")
            print("The thick vegetation prevents you from seeing very far ahead.")
            print("But you continue on,")
            print("...straight into an army of cats...\n")
            print("Your last moments are a flurry of fur and hissing.")
            print("You have failed.")
            try_again()
            break
        elif answer.strip() == "2":
            dirt_path()
            break
        else:
            clear()
            print(f"{answer} Is not valid, please choose again.\n")


def dirt_path():
    """
    First step of the game from going down the correct path.
    """
    clear()
    print("You dash back, away from the growling and through the forest.")
    print("Trying to roient yourself, the sun appears to be low in the sky. It seems like\nevening, and the light is fading as you quickly try to find safety.")
    print("Stumbling through the trees, you run straight onto a small dirt path.")
    print("It leads left, and right.\n")
    while True:
        answer = input("Which way do you go? (left/right): ")
        if answer[0].lower().strip() == "l":
            print("This path is dimly lit, you hear rustling in the bushes...")
            print("The gurilla warfare faction of cats leap from the bushes and attack.\n")
            print("Your last moments are a flurry of fur and bullets.")
            print("You are dead.")
            try_again()
            break
        elif answer[0].lower().strip() == "r":
            stone_passage()
            break
        else:
            clear()
            print(f"{answer} Is not valid, please choose again.\n")


def stone_passage():
    """
    Second step of the game from going down the correct path.
    """
    clear()
    print("This path gets narrower and narrower the farther you go.")
    print("It is getting quite hard to see. You start using your hands to trace the sides\nof the bushes and prevent branches from hitting you as you walk cautiously, but quickly.")
    print("You realise the bushes have gone, as your hands find slick stone at either side,\nand you are now walking through a stone passage way.")
    while True:
        print("Option #1: You keep moving foreward.")
        print("Option #2: You turn back.\n")
        answer = input("Which option will you choose? (1/2): ")
        if answer.strip() == "1":
            cavern()
            break
        elif answer.strip() == "2":
            print("Turning around at this point is no easy feat, but you do it anyway.")
            print("You had a feeling something big and scary was waiting for you,")
            print("...and you're scared of the dark.")
            print("After a long time, you start to see light at the end of the tunnel")
            print("Your eyes take a while to adjust to the brightness,")
            print("But at this relieving sight you sprint towards it blindly")
            print("The first thing you see is a trail of dust, rising up into the air.")
            print("Tracing it's source down to the ground, your eyes fall on a group of\nangry cats, armed to the teeth.\n")
            print("Your last moments are a flurry of fur and dust.")
            print("You are dead.")
            try_again()
            break
        else:
            clear()
            print(f"{answer} Is not valid, please choose again.\n")


def cavern():
    """
    Third step of the game from going down the correct path.
    """
    clear()
    print("You make your way deeper into the tunnel, tripping on stones in utter darkness.")
    print("Slowly you regain vision, a source of light becomes clearer as the tunnel gives\nway to a cavern.")
    print("The cave is dimly lit by a small hole high above in the ceiling, letting in the\nlight of a full moon.")
    print("You spot some illuminated debris on the damp ground.")
    print("On further inspection, you see that someone... lived here?")
    print("Rummaging through a dirty pile of clothes and bedding, you find a backpack with\na knife, an empty gun, and rope inside.")
    print("These may come in handy if things go south.")
    print("For now, you try to get some sleep here before deciding where to go.\n")
    print("You wake up to a much brighter cave, and get ready to go.")
    print("You see two more tunnels at the other end of this space,\nmaybe they lead out of here?\n")
    while True:
        answer = input("Which tunnel do you go through? (left/right): ")
        if answer[0].lower().strip() == "l":
            print("You make your way over to the left tunnel.")
            print("The light slowly disappears as you move forawrds, then it begins to come back,\nfrom a different source...")
            print("It looks like you are approaching a hole in the ground of this tunnel,\nand there is light spilling out of it.")
            print("Once you reach it, you peer down, and wait for your eyes to adjust.")
            print("You see what looks like another cave, but this one is filled with light,\nand must be the way out!")
            print("You look for something to secure your rope to,\nand find a column of stone that will work.")
            print("You abseil down into this cave with ease and delight. Outside you see lush trees\nand hills as you untie your rope.")
            print("You look around the cave, and upon looking a little deeper,\nyou see a grizzly bear.")
            print("It starts to rise... and drool.\n")
            print("Your last moments are a flurry of fur and very, very, big teeth.")
            print("You are dead.")
            try_again()
            break
        elif answer[0].lower().strip() == "r":
            hillside()
            break
        else:
            clear()
            print(f"{answer} Is not valid, please choose again.\n")


def hillside():
    """
    Fourth step of the game from going down the correct path.
    """
    clear()
    print("You head into the tunnel, and after walking some distance in the darkness,\nyou start to get a very bad smell.")
    print("Being more cautious now, you draw your knife, trying to be as quiet as you can.")
    print("Eventually, as the smell gets worse, you start to see some light up ahead.")
    print("You pick up the pace. As you reach the tunnel exit, you see a small pile of fur.")
    print("It seems to be a cat, long dead, wearing a miniature tactical vest strapped with\nammo and a tiny knife.")
    print("You hold your breath and take the ammo, which fits your gun! You load it up and\nkeep a tight grip on it.")
    print("Scanning the area as you move, you make your way uphill to get a good view on\nthe area.")
    print("From the top of the hill, you see a beautiful vally, glowing in the morning sun.")
    print("On a nearby hill, you see a small trail of smoke rising from the trees.")
    print("In the other direction, you see a road leading to a large town.")
    print('"Maybe there are people around, people that can help me!"')
    print("Despite how hungry and tired you are, you are now filled with hope.")
    while True:
        print("Option #1: You go to the smoke on the hill.")
        print("Option #2: You go down to the road and into the town.\n")
        answer = input("Which option will you choose? (1/2): ")
        if answer.strip() == "1":
            camp()
            break
        elif answer.strip() == "2":
            print("Your are dead.")
            try_again()
            break
        else:
            clear()
            print(f"{answer} Is not valid, please choose again.\n")


if __name__ == "__main__":
    clear()
    welcome()
