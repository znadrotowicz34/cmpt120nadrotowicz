# pi.py
# A program that approximates the value of pi

def main():
    import math

    n = eval(input("Enter the number of terms to sum:"))

    pi = 0
    for i in range (1, n+1, 2):
        pi += 4 / i - 4 / (i+2)
    print (pi)

    print (pi-math.pi)
    
    
    
main()
