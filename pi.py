# pi.py
# A program that approximates the value of pi

def main():
    import math

    n = eval(input("Enter the number of terms to sum:"))

    pi = 0
    sign = 1
    for i in range (1, n*2, 2):
        pi += sign * (4 / i)
        sign = -sign
    print (pi)

    print (math.pi - pi)
    
    
    
main()
