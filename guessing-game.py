#guessing-game.py
#A simple guessing game

def main():

    animalCorrect = 0

    while animalCorrect == 0:
        animal = input("I am thinking of an animal. What animal am I thinking of?")
        if animal == "Panda":
            print("Correct!")
            animalCorrect = 1
        else:
            print("Wrong animal")
        
main()
