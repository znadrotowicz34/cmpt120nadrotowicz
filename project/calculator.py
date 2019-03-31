#calculator.py
#creates the GUI for the calculator

from graphics import *
from calc_functions import *
 
def calculatorGUI():
    #create window
    win = GraphWin("Calculator",500,200)
    win.setBackground('light blue')

    #create objects
    basicCalculator = Text(Point(250,20),"Basic Calculator")
    basicCalculator.setSize(20)
    basicCalculator.draw(win)

    enterText = Text(Point(250,75),"Enter equation with spaces in between numbers and operators.")
    enterText.setSize(12)
    enterText.draw(win)

    equationBox = Entry(Point(250,120),20)
    equationBox.draw(win)
    
    
    readyButton = Rectangle(Point(200,150),Point(300,175))
    readyButton.setFill('black')
    readyButton.draw(win)

    calculateText = Text(Point(250,162.5),"Calculate")
    calculateText.setTextColor('white')
    calculateText.draw(win)

    #calculate equation on GUI
    win.getMouse()

    equationText = equationBox.getText()
    calculateText.undraw()
    readyButton.undraw()
    
    answer = calculateAnswer(equationText)

    answerText = Text(Point(250,162.5),"The answer is " + str(answer))
    answerText.draw(win)

    
def main():
    calculatorGUI()
main()
<<<<<<< HEAD
=======
<<<<<<< HEAD
    
=======
>>>>>>> ad816677cbb00d079f81b8d070f1697bdd5f556f
>>>>>>> 345c98bd3ea1d638e9b7aaf34f23e665215fb02e
