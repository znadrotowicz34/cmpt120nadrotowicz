# fibonacci.py
# A program that computes the nth Fibonacci number where n is a value by the user

def main():
    n = eval(input("Enter an integer:"))

    a,b = 1,1

    for i in range (n - 2):
        a,b = a+b, a
    print (a)
  
   
main()
