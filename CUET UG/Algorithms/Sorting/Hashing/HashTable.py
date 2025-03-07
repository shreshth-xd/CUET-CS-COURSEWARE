# Implementing Hashing in Python using lists and classes
import csv

class HashMap:
    def __init__(self,size=100):
        self.MAX = size
        self.arr = [None for i in range(self.MAX)]
    
    def getHash(self,key):
        sum=0
        for i in key:
            sum+=ord(i)
        
        hash=sum%10
        return hash

    def add(self,key,value):
        index=self.getHash(key)
        self.arr[index] = value
    
    # Introducing this additional function to export the data provided by the user to the csv file
    def exportData(self,filename,key,value):
        with open(filename,"a") as file:
            writer1 = csv.writer(filename)
            writer1.writerow(key,value)

    def get(self,key):
        index=self.getHash(key)
        return self.arr[index]

# Making a recordHandler object from HashMap class:
recordHandler = HashMap()
data = {}

with open ("Sturec.csv","r") as file:
    for line in file:
        tokens = line.split(",")
        name=tokens[0]
        marks=tokens[1]
        recordHandler.add(name,marks)
        data[name]=marks

while True:
    print("1. Display marks of a particular student: ")
    print("2. Display the list of all students with their respective marks: ")
    print("3. Add more data items: ")
    print("4. Exit")
    choice=int(input(">"))

    if choice==1:
        ask=input("Enter the name of that student: ")
        marks_=recordHandler.get(ask)
        print(ask,"has obtained",marks_,"marks out of 100.")
    elif choice==2:
        print(data)
    elif choice==3:
        ask=input("Enter the name of that student: ")
        marks_=int(input("Enter marks obtained by him/her out of 100: "))
        recordHandler.add(ask,marks_)
        recordHandler.exportData("Sturec.csv")
    elif choice==4:
        break
    else:
        print("Please make a valid choice.")