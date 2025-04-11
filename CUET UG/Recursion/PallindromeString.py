# Checking if a given string is a pallindrome or not
string=str(input("Enter the string: "))

def PallindromeString(string):
    string = "".join(c.lower() for c in string if c.isalnum())

    def checkForPallindrome(left=0,right=len(string)-1):
        if string=="":
            return True
        elif len(string)==1:
            return True
        elif string[0]!=string[len(string)-1]:
            return False
        
        return checkForPallindrome(left+1,right-1)
    
    return checkForPallindrome()

