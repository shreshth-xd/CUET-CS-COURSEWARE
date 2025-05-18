# Basic program of try-except clause for exception handling
n=int(input("Enter a number: "))
try:
    print("I will see if there is any error :)")
    print(1/n)
except ZeroDivisionError:
    print("Division by 0 is undefined")