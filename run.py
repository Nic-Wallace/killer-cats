# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


print("You wake up, surrounded by trees and very confused.")
print('"How did I get here?"')
print("Your head hurts, you\'re covered in scratches.")
print("You hear growling in front of you. It almost seems... familiar.")
print("But you can't quite remember what heppened.")
print("Option #1: Creep towards the growling to investigate.")
print("Option #2: Run away from the growling as fast as possible.")

answer = input("Which option will you choose? (1/2)")
if answer.strip() == "1":

    print("You creep towards the growling.")
    print("The thick vegetation prevents you from seeing very far ahead.")
    print("But you continue on,")
    print("...straight into an army of cats...")
    print("Your last moments are a flurry of fur and hissing.")
    print("You have failed.")

    answer = input("Would you like to try again? (yes/no)")

    if answer.lower().strip() == "y":

elif answer.strip() == "2":

    print("You sprint back, away from the growling.")
    print("Stumbling through the forest, you find a small dirt path.")
    print("It leads left, and right.")

    answer = input("Which way do you go? (left/right)")
 


