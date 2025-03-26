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
        with open("StudentRecord.dat","ab") as file:
            pickle.dump(rec,file)

        ask=str(input("You've got more records? "))
        if "yes" in ask.lower():
            continue
        elif "no" in ask.lower():
            break
        else:
            print("Answer in yes or no.")

    
    elif choice==2:
        with open("StudentRecord.dat","rb") as file:
            name = str(input("Enter the student's name: "))
            while True:        
                try:
                    data=pickle.load(file)
                    print(data)
                    if name in data.keys():
                        found=True
                except EOFError:
                    if found==False:
                        print("Record not found.")
                    else:
                        print("Record found!")
                        break

    elif choice==3:
        break
    
    else:
        print("Please, make a valid choice.")