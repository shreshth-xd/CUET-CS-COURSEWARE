# Implementing chaining method for collision resolution in Hash maps/Hash tables in Python
import csv

class HashTable:
    def __init__(self,size=100):
        self.MAX=size
        self.arr = [[] for i in range(self.MAX)]
    
    def GetHash(self,key):
        HashValue=0
        for i in key:
            HashValue+=ord(i)
        return HashValue
    
    def ExportData(self,filename,key,value):
        with open(filename,"a") as file:
            writer_ = csv.writer(file)
            writer_.writerow([key,value])
    
    def add(self,key,value):
        h=self.GetHash(key)
        found=False
        for idx,element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[h][idx] = (key,value)
                
                # Making the same change on the CSV file so as to keep the file updated
                with open("Sturec.csv","r") as infile ,open("Sturec.csv","w") as outfile:
                    writer_ = csv.writer(outfile)
                    reader = csv.writer(infile)
                    for line in reader:
                        tokens=line.split()
                        name=tokens[0]
                        marks=tokens[1]
                        if name!=key:
                            writer_.writerow([name,marks])
                        else:
                            writer_.writerow([key,marks])
                found=True
                break

        if not found:
            self.arr[h].append((key,value))
            self.ExportData("Sutrec.csv",key,value)


    def get(self,key):
        h=self.GetHash(key)
        for idx,element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                return element[1]
            
    
    # To delete a key value pair from the Hash table
    def delItem(self,key):
        hash=self.GetHash(key)
        for index,element in enumerate(self.arr[hash]):
            if len(element)==2 and element[0]==key:
                del self.arr[hash][index]

                # Making the same change on the CSV file so as to keep the file updated
                with open("Sturec.csv","r") as infile, open("Sturec.csv","r") as outfile:
                    writer_ = csv.writer(outfile)
                    reader = csv.writer(infile)
                    for line in reader:
                        tokens=line.split()
                        name=tokens[0]
                        marks=tokens[1]
                        if name!=key:
                            writer_.writerow([name,marks])                          


# Creating a record handler object out of Hash table class
RecordHandler = HashTable()
data={}

with open ("Sturec.csv","r") as file:
    for single_line in file:
        tokens = single_line.split()
        name=tokens[0]
        marks=int(tokens[1])
        RecordHandler.add(name,marks)
        data[name] = marks

print("1. Display data of all the students")
print("2. Display marks of a particular student")
print("3. Add more data points")
print("4. Edit a student's marks")
print("5. Delete a data point")
print("6. Exit")

while True:
    choice=int(input("Enter your choice: "))
    if choice==1:
        print(data)     
    elif choice==2:
        name=input("Enter the name of the student: ")
        print(RecordHandler.get(name))
    elif choice==3:
        name=input("Enter the name of the new student: ")
        marks=int(input("Enter the marks: "))
        RecordHandler.add(name,marks)
    elif choice==4:
        name=input("Enter the name of the student to edit his/her marks: ")
        new_marks = int(input("Enter the new marks: "))
        RecordHandler.add(name,new_marks)
    elif choice==5:
        name=input("Enter the name of the student to delete his/her data: ")
        RecordHandler.delItem(name)
    elif choice==6:
        break
    else:
        print("Please make a valid choice.")