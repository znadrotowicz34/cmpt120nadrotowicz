#calc_functions.py
#stores all calculator functions

from math import *

def calculateAnswer(inputText):

    #take equation from user
    equationList = inputText.rsplit()
<<<<<<< HEAD
    print(equationList)
=======
>>>>>>> ad816677cbb00d079f81b8d070f1697bdd5f556f
    
    #sets variable for while loop
    keepGoing = 1
    
    #while loop
    while keepGoing == 1:
        multiplyDivideFlag = 0
        try:
            multiplyPosition = equationList.index("*")
        except ValueError:
            multiplyPosition = 9999
        try:
            dividePosition = equationList.index("/")
        except ValueError:
            dividePosition = 9999
        try:
            addPosition = equationList.index("+")
        except ValueError:
            addPosition = 9999
        try:
            subtractPosition = equationList.index("-")
        except ValueError:
            subtractPosition = 9999
        

        
        #multiplication
        if dividePosition > multiplyPosition:
            print("Multiply")
            multiplyDivideFlag = 1
            number1 = equationList[multiplyPosition - 1]
            number2 = equationList[multiplyPosition + 1]
            number3 = float(number1) * float(number2)
            del equationList[multiplyPosition - 1: multiplyPosition + 2]
            #the following line was there to test if the proper number was being inserted at the proper place
            #print("inserting " + str(number3) + "at index " + str(multiplyPosition - 1))
            equationList.insert(multiplyPosition - 1,number3)
            if len(equationList) == 1:
                #the following line is there to test if the equation list was proper
                #print(equationList)
                keepGoing = 0
        elif multiplyPosition > dividePosition:
            print("Divide")
            multiplyDivideFlag = 1
            number1 = equationList[dividePosition - 1]
            number2 = equationList[dividePosition + 1]
            number3 = float(number1) / float(number2)
            del equationList[dividePosition - 1: dividePosition + 2]
            #print("inserting " + str(number3) + "at index " + str(dividePosition - 1))
            equationList.insert(dividePosition - 1,number3)
            if len(equationList) == 1:
              #print(equationList)
              keepGoing = 0
        #division 

                
        #tests to see if the string no longer has multiplication or division
        if multiplyDivideFlag != 1:

            #addition
            if  subtractPosition > addPosition:
                print("Add")
                number1 = equationList[addPosition - 1]
                number2 = equationList[addPosition + 1]
                number3 = float(number1) + float(number2) 
                del equationList[addPosition - 1: addPosition + 2]
                #print("inserting " + str(number3) + "at index " + str(addPosition - 1))
                equationList.insert(addPosition - 1,number3)
                if len(equationList) == 1:
                    #print(equationList)
                    keepGoing = 0
            elif addPosition > subtractPosition:
                print("Subtract")
                number1 = equationList[subtractPosition - 1]
                number2 = equationList[subtractPosition + 1]
                number3 = float(number1) - float(number2)
                del equationList[subtractPosition - 1: subtractPosition + 2]
                #print("inserting " + str(number3) + "at index " + str(subtractPosition - 1))
                equationList.insert(subtractPosition - 1,number3)
                if len(equationList) == 1:
                    #print(equationList)
                    keepGoing = 0

    #return answer to user    
    return number3
