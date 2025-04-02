# Using Recursion to find if a given number is a prime number or not

"""
Using the √n logic to find if the number is prime or not.
According to this logic if a number does not have any factor less than √n then it will never have a factor
between 2 and n-1, which means that the number will be a prime number in this case.

"""
def PrimeTest(n):
    if n==0 or n==1 or n<0:
        return 0
    elif n==2 or n==3:
        return 1