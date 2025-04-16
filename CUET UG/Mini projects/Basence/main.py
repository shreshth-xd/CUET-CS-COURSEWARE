# __name__==__main__ 
# Main script for the Data Analyzer and probability calculator project
# This analyzer currently works only for the purpose of analyzing the performance of students of a class
# Currently using and relying on CSV for data storage
import mysql.connector as connector
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
        names=[]
        IndividualScores={}
        averages=[]
        
        stream = str(input("Enter the stream: "))
        strengthOfClass = int(input("Enter the number of students in this class: "))
        subjects=int(input("Enter the number of subjects and electives for this stream: "))

        for i in range(strengthOfClass):
            name=str(input("Enter the name of the student: "))
            # scores=
        
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