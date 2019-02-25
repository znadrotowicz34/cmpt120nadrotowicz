#calc_functions.py
#stores all calculator functions

from graphics import *
from math import *
import calculator

def calc_Functions():

    calculator.equationText = calculator.equationBox.getText()

    equationList = equationText.rsplit()
    print(equationList)
    
    while True:
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
        

        print(multiplyPosition)
        print(dividePosition)
        print(addPosition)
        print(subtractPosition)
    
        if dividePosition > multiplyPosition:
            print("Multiply")
            multiplyDivideFlag = 1
            number1 = equationList[multiplyPosition - 1]
            #print(number1)
            number2 = equationList[multiplyPosition + 1]
            #print(number2)
            number3 = float(number1) * float(number2)
            #print(number3)
            #print(equationList)
            del equationList[multiplyPosition - 1: multiplyPosition + 2]
            #print(equationList)
            print("inserting " + str(number3) + "at index " + str(multiplyPosition - 1))
            equationList.insert(multiplyPosition - 1,number3)
            print(equationList)
            #print("the list is now" + str(equationList))
            if len(equationList) == 1:
                #print("this should be right")
                print(equationList)
                break
        elif multiplyPosition > dividePosition:
            print("Divide")
            multiplyDivideFlag = 1
            number1 = equationList[dividePosition - 1]
            #print(number1)
            number2 = equationList[dividePosition + 1]
            #print(number2)
            number3 = float(number1) / float(number2)
            #print(number3)
            del equationList[dividePosition - 1: dividePosition + 2]
            print("inserting " + str(number3) + "at index " + str(dividePosition - 1))
            equationList.insert(dividePosition - 1,number3)
            print(equationList)
            if len(equationList) == 1:
                print(equationList)
                break

        if multiplyDivideFlag != 1:

            if  subtractPosition > addPosition:
                print("Add")
                number1 = equationList[addPosition - 1]
                #print(number1)
                number2 = equationList[addPosition + 1]
                #print(number2)
                number3 = float(number1) + float(number2) 
                #print(number3)
                del equationList[addPosition - 1: addPosition + 2]
                print("inserting " + str(number3) + "at index " + str(addPosition - 1))
                equationList.insert(addPosition - 1,number3)
                print(equationList)
                if len(equationList) == 1:
                    print(equationList)
                    break
            elif addPosition > subtractPosition:
                print("Subtract")
                number1 = equationList[subtractPosition - 1]
                #print(number1)
                number2 = equationList[subtractPosition + 1]
                #print(number2)
                number3 = float(number1) - float(number2)
                #print(number3)
                del equationList[subtractPosition - 1: subtractPosition + 2]
                print("inserting " + str(number3) + "at index " + str(subtractPosition - 1))
                equationList.insert(subtractPosition - 1,number3)
                print(equationList)
                if len(equationList) == 1:
                    print(equationList)
                    break

calc_Functions()
