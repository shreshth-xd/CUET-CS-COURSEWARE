def Hailstone(n):
    if n>0:
        if n%2==0:
            print(n)
            Hailstone(n/2)
        else:
            print(n)
            Hailstone(3*n+1)
    if n==1:
        print(n)
        return
    else:
        print("The Hailstone sequence begins with a positive integer, no negative integer is allowed.")