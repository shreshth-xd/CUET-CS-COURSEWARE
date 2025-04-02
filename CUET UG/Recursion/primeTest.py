# Using Recursion to find if a given number is a prime number or not

def PrimeTest(n):
    if n==0 or n==1 or n<0:
        return 0
    elif n==2 or n==3:
        return 1