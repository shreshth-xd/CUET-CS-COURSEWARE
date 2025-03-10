"""
The Hailstone sequence starts with a positive integer n and is proceeded by using two rules, if n is even
then the next number on the sequence is n/2, if the number is odd then the next number on the sequence is
3*n+1, and so on the process is repeated, however, we have to add the base case in this recursive function 
for the case where the number is or gets deduced to 1 at any point of the sequence otherwise without this
we would obtain an infinitely recurring sequence which is of course not we actually want.
"""

def Hailstone(n):
    if n==1:
        print(n)
        return
    if n>0:
        if n%2==0:
            print(n,end=" ")
            Hailstone(n//2)
        else:
            print(n,end=" ")
            Hailstone(3*n+1)
    else:
        print("The Hailstone sequence begins with a positive integer, no negative integer is allowed.")

n=int(input("Enter the number to start the Hailstone sequence: "))
Hailstone(n)