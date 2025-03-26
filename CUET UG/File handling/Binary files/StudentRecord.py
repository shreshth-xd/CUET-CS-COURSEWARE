# Using Pickle module for pushing and retrieving data from the Binary file
import pickle

while True:
    print("1. Push data to the file")
    print("2. Retrieve data from the file")
    print("3. Exit")
    choice=int(input("Enter your choice: "))

    if choice==1:
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

        with open("StudentRecord.dat","ab") as file:
            pickle.dump(rec,file)
    
    elif choice==2:
        with open("StudentRecord.dat","rb") as file:
            data=pickle.load(file)
            name = str(input("Enter the student's name: "))
            if name in data.keys():
                print("Record found!")
                print(data[name])
            else:
                print("Data not found.")

    elif choice==3:
        break
    
    else:
        print("Please, make a valid choice.")