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