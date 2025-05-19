n=int(input("Enter a number: "))
n1=int(input("Enter another number: "))
try:
    # To execute the code block where there is a possibility for an exception or error to be encountered 
    print("Oh boy, let's check for some errors.")
    n/n1
except ValueError:
    # To tackle a certain exception by writing a code block to be executed whenever that certain exception is raised
    # In technical terms it is also known as, "catching of an exception" 
    print("Please don't enter a string when you are asked for a freaking number!!!!")
except ZeroDivisionError:
    print("That's undefined bro")
else:
    # This code block gets executed when the code block is executed without any exception or error
    print("Congratulations you just did it without encountering any error.")
finally:
    # This code block gets executed irrespective of whether any exception has been raised or not
    print("Don't worry, you would have to encounter me in either way.")