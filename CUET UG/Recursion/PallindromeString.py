# Checking if a given string is a pallindrome or not
string=str(input("Enter the string: "))

def PallindromeString(string):
    string = "".join(c.lower() for c in string if c.isalnum())

    if string=="":
        return True
    elif len(string)==1:
        return True
    elif string[0]!=string[len(string)-1]:
        return False