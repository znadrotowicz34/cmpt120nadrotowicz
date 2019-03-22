# calculator.py
# Creates a basic calculator

from graphics import *
from calc_functions import *

def main():

    #create window
    win = GraphWin("Calculator",300,460) 
    win.setBackground('light blue')

    #set numbers and symbols
    rectangle1 = Rectangle(Point(40,80), Point(80,120))
    rectangle1.setFill("black")
    rectangle1.draw(win)
    text7 = Text(Point(60,100), "7")
    text7.setTextColor("white")
    text7.setSize(18)
    text7.draw(win)
    
    rectangle2 = Rectangle(Point(40,160), Point(80,200))
    rectangle2.setFill("black")
    rectangle2.draw(win)
    text4 = Text(Point(60,180), "4")
    text4.setTextColor("white")
    text4.setSize(18)
    text4.draw(win)

    rectangle3 = Rectangle(Point(40,240), Point(80,280))
    rectangle3.setFill("black")
    rectangle3.draw(win)
    text1 = Text(Point(60,260), "1")
    text1.setTextColor("white")
    text1.setSize(18)
    text1.draw(win)

    rectangle4 = Rectangle(Point(40,320), Point(80,360))
    rectangle4.setFill("black")
    rectangle4.draw(win)
    text0 = Text(Point(60,340), "0")
    text0.setTextColor("white")
    text0.setSize(18)
    text0.draw(win)

    rectangle5 = Rectangle(Point(100,80), Point(140,120))
    rectangle5.setFill("black")
    rectangle5.draw(win)
    text8 = Text(Point(120,100), "8")
    text8.setTextColor("white")
    text8.setSize(18)
    text8.draw(win)

    rectangle6 = Rectangle(Point(100,160), Point(140,200))
    rectangle6.setFill("black")
    rectangle6.draw(win)
    text5 = Text(Point(120,180), "5")
    text5.setTextColor("white")
    text5.setSize(18)
    text5.draw(win)

    rectangle7 = Rectangle(Point(100,240), Point(140,280))
    rectangle7.setFill("black")
    rectangle7.draw(win)
    text2 = Text(Point(120,260), "2")
    text2.setTextColor("white")
    text2.setSize(18)
    text2.draw(win)

    rectangle8 = Rectangle(Point(100,320), Point(140,360))
    rectangle8.setFill("black")
    rectangle8.draw(win)
    textDot = Text(Point(120,340), ".")
    textDot.setTextColor("white")
    textDot.setSize(18)
    textDot.draw(win)

    rectangle9 = Rectangle(Point(160,80), Point(200,120))
    rectangle9.setFill("black")
    rectangle9.draw(win)
    text9 = Text(Point(180,100), "9")
    text9.setTextColor("white")
    text9.setSize(18)
    text9.draw(win)

    rectangle10 = Rectangle(Point(160,160), Point(200,200))
    rectangle10.setFill("black")
    rectangle10.draw(win)
    text6 = Text(Point(180,180), "6")
    text6.setTextColor("white")
    text6.setSize(18)
    text6.draw(win)

    rectangle11 = Rectangle(Point(160,240), Point(200,280))
    rectangle11.setFill("black")
    rectangle11.draw(win)
    text3 = Text(Point(180,260), "3")
    text3.setTextColor("white")
    text3.setSize(18)
    text3.draw(win)

    rectangle12 = Rectangle(Point(160,320), Point(200,360))
    rectangle12.setFill("red")
    rectangle12.draw(win)
    textEqual = Text(Point(180,340), "=")
    textEqual.setTextColor("white")
    textEqual.setSize(18)
    textEqual.draw(win)

    rectangle13 = Rectangle(Point(220,80), Point(260,120))
    rectangle13.setFill("green")
    rectangle13.draw(win)
    textDivide = Text(Point(240,100), "/")
    textDivide.setTextColor("white")
    textDivide.setSize(18)
    textDivide.draw(win)

    rectangle14 = Rectangle(Point(220,160), Point(260,200))
    rectangle14.setFill("green")
    rectangle14.draw(win)
    textMultiply = Text(Point(240,180), "*")
    textMultiply.setTextColor("white")
    textMultiply.setSize(18)
    textMultiply.draw(win)

    rectangle15 = Rectangle(Point(220,240), Point(260,280))
    rectangle15.setFill("green")
    rectangle15.draw(win)
    textSubtraction = Text(Point(240,260), "-")
    textSubtraction.setTextColor("white")
    textSubtraction.setSize(18)
    textSubtraction.draw(win)

    rectangle16 = Rectangle(Point(220,320), Point(260,360))
    rectangle16.setFill("green")
    rectangle16.draw(win)
    textAddition = Text(Point(240,340), "+")
    textAddition.setTextColor("white")
    textAddition.setSize(18)
    textAddition.draw(win)

    rectangle17 = Rectangle(Point(160,400), Point(200,440))
    rectangle17.setFill("red")
    rectangle17.draw(win)
    textNegative = Text(Point(180,420), "+/-")
    textNegative.setTextColor("white")
    textNegative.setSize(15)
    textNegative.draw(win)

    rectangle18 = Rectangle(Point(220,400), Point(260,440))
    rectangle18.setFill("red")
    rectangle18.draw(win)
    textDelete = Text(Point(240,420), "Del")
    textDelete.setTextColor("white")
    textDelete.setSize(15)
    textDelete.draw(win)
    
    rectangleTop = Rectangle(Point(40,10), Point(260,60))
    rectangleTop.setFill("white")
    rectangleTop.draw(win)

    # check for keys

    keepGoing = 1
    stringLength = 0
    
    equationString = ""
    print(equationString)

    while keepGoing == 1:
        click = win.getMouse()
        print(click)
        x,y = click.getX(), click.getY()
        ur, ll = x, y
        print (ur, ll)
        if ur > 40 and ur < 80 and ll > 80 and ll < 120:
            seven = Text(Point(50 + stringLength * 7,35),"7")
            seven.setSize(20)
            seven.draw(win)
            print("seven")
            tempString = equationString
            equationString = tempString + "7"
            print(equationString)
        elif ur > 40 and ur < 80 and ll > 160 and ll < 200:
            four = Text(Point(50 + stringLength * 7,35),"4")
            four.setSize(20)
            four.draw(win)
            print("four")
            tempString = equationString
            equationString = tempString + "4"
            print(equationString)
        elif ur > 40 and ur < 80 and ll > 240 and ll < 280:
            one = Text(Point(50 + stringLength * 7,35),"1")
            one.setSize(20)
            one.draw(win)
            print("one")
            tempString = equationString
            equationString = tempString + "1"
            print(equationString)
        elif ur > 40 and ur < 80 and ll > 320 and ll < 360:
            zero = Text(Point(50 + stringLength * 7,35),"0")
            zero.setSize(20)
            zero.draw(win)
            print("zero")
            tempString = equationString
            equationString = tempString + "0"
            print(equationString)
        elif ur > 100 and ur < 140 and ll > 80 and ll < 120:
            eight = Text(Point(50 + stringLength * 7,35),"8")
            eight.setSize(20)
            eight.draw(win)
            print("eight")
            tempString = equationString
            equationString = tempString + "8"
            print(equationString)
        elif ur > 100 and ur < 160 and ll > 140 and ll < 200:
            five = Text(Point(50 + stringLength * 7,35),"5")
            five.setSize(20)
            five.draw(win)
            print("five")
            tempString = equationString
            equationString = tempString + "5"
            print(equationString)
        elif ur > 100 and ur < 140 and ll > 240 and ll < 280:
            two = Text(Point(50 + stringLength * 7,35),"2")
            two.setSize(20)
            two.draw(win)
            print("two")
            tempString = equationString
            equationString = tempString + "2"
            print(equationString)
        elif ur > 100 and ur < 140 and ll > 320 and ll < 360:
            dot = Text(Point(50 + stringLength * 7,35),".")
            dot.setSize(16)
            dot.draw(win)
            print("dot")
            tempString = equationString.strip()
            equationString = tempString + "."
            print(equationString)
        elif ur > 160 and ur < 200 and ll > 80 and ll < 120:
            nine = Text(Point(50 + stringLength * 7,35),"9")
            nine.setSize(20)
            nine.draw(win)
            print("nine")
            tempString = equationString
            equationString = tempString + "9"
            print(equationString)
        elif ur > 160 and ur < 200 and ll > 160 and ll < 200:
            six = Text(Point(50 + stringLength * 7,35),"6")
            six.setSize(20)
            six.draw(win)
            print("six")
            tempString = equationString
            equationString = tempString + "6"
            print(equationString)
        elif ur > 160 and ur < 200 and ll > 240 and ll < 280:
            three = Text(Point(50 + stringLength * 7,35),"3")
            three.setSize(20)
            three.draw(win)
            print("three")
            tempString = equationString
            equationString = tempString + "3"
            print(equationString)
        elif ur > 220 and ur < 260 and ll > 80 and ll < 120:
            divide = Text(Point(50 + stringLength * 7,35),"/")
            divide.setSize(20)
            divide.draw(win)
            print("divide")
            tempString = equationString
            equationString = tempString + " / "
            print(equationString)
        elif ur > 220 and ur < 260 and ll > 160 and ll < 200:
            multiply = Text(Point(50 + stringLength * 7,35),"*")
            multiply.setSize(20)
            multiply.draw(win)
            print("multiply")
            tempString = equationString
            equationString = tempString + " * "
            print(equationString)
        elif ur > 220 and ur < 260 and ll > 240 and ll < 280:
            subtract = Text(Point(50 + stringLength * 7,35),"-")
            subtract.setSize(20)
            subtract.draw(win)
            print("subtract")
            tempString = equationString
            equationString = tempString + " - "
            print(equationString)
        elif ur > 220 and ur < 260 and ll > 320 and ll < 360:
            add = Text(Point(50 + stringLength * 7,35),"+")
            add.setSize(20)
            add.draw(win)
            print("add")
            tempString = equationString
            equationString = tempString + " + "
            print(equationString)
        elif ur > 160 and ur < 200 and ll > 400 and ll < 440:
            negative = Text(Point(50 + stringLength * 7,35),"-")
            negative.setSize(16)
            negative.draw(win)
            print("negative")
            tempString = equationString
            equationString = tempString + "-"
            print(equationString)
        elif ur > 220 and ur < 260 and ll > 400 and ll < 440:
            resetBox = Rectangle(Point(40,10), Point(260,60))
            resetBox.setFill("white")
            resetBox.draw(win)
            equationString = ""
            stringLength = 0
            print("delete")
            print(equationString)
        elif ur > 160 and ur < 200 and ll > 320 and ll < 360:
            print(equationString)
            keepGoing = 0
        stringLength = stringLength + 2


    answer = calculateAnswer(equationString)
    answerText = Text(Point(230,35), answer)
    answerText.setTextColor("green")
    answerText.setSize(20)
    answerText.draw(win)
    print(str(answer))
        
    
     
main()
