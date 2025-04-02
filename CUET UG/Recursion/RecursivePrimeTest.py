# Using Recursion to find if a given number is a prime number or not

"""
# NOTE: Always keep in mind to use the return statement while making a recursive call inside that function, Thank me later.


Using the √n logic to find if the number is prime or not.
According to this logic if a number does not have any factor less than √n then it will never have a factor
between 2 and n-1, which means that the number will be a prime number in this case.
"""
def PrimeTest(n,i=2):
    if n==0 or n==1 or n<0:
        return 0
    elif n==2 or n==3:
        return 1
    else:
        if i<=n**(1/2):
            if n%i==0:
                return 0
            else:
                return PrimeTest(n,i=i+1)
        else:
            return 1

number=int(input("Enter the number to check if it's a prime or not: "))
response=PrimeTest(number)
if response==0:
    print("No, It's not a prime number.")
else:
    print(response)
    print("Yes, it's a prime number.")