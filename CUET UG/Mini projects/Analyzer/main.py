# __name__==__main__ 
# Main script for the Data Analyzer and probability calculator project
import matplotlib
import csv
from collections import Counter


while True:
    print("1. Upload dataset")
    print("2. Generate frequency table")
    print("3. Calculate probability")
    print("4. Plot graph")
    print("5. Export report")
    print("6. Exit")
    choice=int(input(">"))
    if choice==1:
        pass
    elif choice==5:
        print("Export it in: ")
        print("1. pdf")
        print("2. docx")
        print("3. png")
        print("4. jpeg")
        print("5. svg")
        format_=str(input(">"))
        pass
    elif choice==6:
        break
    else:
        print("Please make a valid choice.")