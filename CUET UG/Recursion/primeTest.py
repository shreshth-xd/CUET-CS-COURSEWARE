# Using recursion to find if a given number is prime or not.

def primeTest(n,i=2):
    if n==1 or n==0 or n<0:
        return 0
    else:
        # Instead of iterating all over from 2 to n to check for possible factors of n
        # We will just check from 2 to √n to check for possible factors of n
        if i<=n**(1/2):

            if n%i==0:
                return 1
            else:
                return primeTest(n,i+1)
        else:
            return 0

n=int(input("Enter the number to check if it's a prime number or not: "))
res=primeTest(n)
if res==1:
    print("Yes!",n,"is a prime number.")
else:
    print("No!",n,"is not a prime number.")

        