# Checking if a given string is a pallindrome or not
string=str(input("Enter the string: "))

def PallindromeString(string):
    if string=="":
        return True
    elif len(string)==1:
        return True
    