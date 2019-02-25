# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Zachary Nadrotowicz
# Created: 2019-02-25
    # get user's first and last names

def notStrong(passwd):
    if len(passwd) < 8:
        return True
    elif passwd.lower() == passwd:
        return True
    elif passwd.upper() == passwd:
        return True
    else:
        return False

def getName():
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    return [first,last]
    # TODO modify this to generate a Marist-style username
def maristUname(name):
    uname = (name[0] + "." + name[1]).lower()
    return uname
    # ask user to create a new password
def getPasswd():
    passwd = input("Create a new password: ")
    # TODO modify this to ensure the password has at least 8 characters
    while notStrong(passwd):
        print("Fool of a Took! That password is feeble!")
        passwd = input("Create a new password: ")
    return passwd
          
                       

def main():
    name = getName()
    uname = maristUname(name)
    passwd = getPasswd()
    print("The force is strong in this one…")
    print("Account configured. Your new email address is " + uname + "@marist.edu")
main()

