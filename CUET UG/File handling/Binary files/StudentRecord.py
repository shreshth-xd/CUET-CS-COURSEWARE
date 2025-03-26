# Using Pickle module for pushing and retrieving data from the Binary file
import pickle

while True:
    name = str(input("Enter the student's name: "))
    marks = int(input("Enter his/her marks: "))
    rec={}
    rec[name] = marks

    ask=str(input("You've got more records? "))
    if "yes" in ask.lower():
        continue
    elif "no" in ask.lower():
        break
    else:
        print("Answer in yes or no.")