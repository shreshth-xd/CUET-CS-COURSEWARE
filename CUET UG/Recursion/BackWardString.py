# Using Recursion to print a string backwards to understand how nested call stacks in recursion actually works:

string = str(input("Enter the string: "))

def bkwrds(string, n=0):
    if n==len(string):
        return
    
    bkwrds(string,n+1)
    print(string[n], end="")
    return 

bkwrds(string)