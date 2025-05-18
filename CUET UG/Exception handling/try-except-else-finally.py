n=int(input("Enter a number: "))
n1=int(input("Enter another number: "))
try:
    print("Oh boy, let's check for some errors.")
    n/n1
except ValueError:
    print("Please don't enter a string when you are asked for a freaking number!!!!")
except ZeroDivisionError:
    print("That's undefined bro")
else:
    print("Congratulations you just did it without encountering any error.")