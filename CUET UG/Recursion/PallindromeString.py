# Checking if a given string is a pallindrome or not
string=str(input("Enter the string: "))

def PalindromeString(string):
    # string = "".join(c.lower() for c in string if c.isalnum())
    string = string.lower()

    def checkForPalindrome(left=0,right=len(string)-1):
        if left>=right:
            return True
        elif string[left]!=string[right]:
            return False
        
        return checkForPalindrome(left+1,right-1)
    
    return checkForPalindrome()

result=PalindromeString(string)
if result==True:
    print("Yes!, the string is pallindrome.")
else:
    print("No, the string not a pallindrome.")