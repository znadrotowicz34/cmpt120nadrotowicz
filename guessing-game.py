#guessing-game.py
#A simple guessing game

def main():

    animalCorrect = 0

    while animalCorrect == 0:
        animal = input("I am thinking of an animal. What animal am I thinking of?" )
        answer = animal.lower()
        if answer == "panda":
            print("Correct!")
            animalCorrect = 1
            likeness = input("Do you like this animal? ")
            if likeness == "yes":
                print("It is a cool animal!")
            elif likeness == "no":
                print("I understand not all animals are liked.")
            else:
                print("I guess I'll never know if you like pandas or not")
        elif answer[0] == "q":
            print("You have quit the game.")
            animalCorrect = 1
        else:
            print("Wrong animal")
        
main()
