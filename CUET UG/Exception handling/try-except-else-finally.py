n=int(input("Enter a number: "))
n1=int(input("Enter another number: "))
try:
    # To execute the code block where there is a possibility for an exception or error to be encountered 
    print("Oh boy, let's check for some errors.")
    n/n1
except ValueError:
    # To tackle a certain exception by writing a code block to be executed whenever that certain exception is raised
    print("Please don't enter a string when you are asked for a freaking number!!!!")
except ZeroDivisionError:
    print("That's undefined bro")
else:
    print("Congratulations you just did it without encountering any error.")
finally:
    print("Don't worry, you would have to encounter me in either way.")