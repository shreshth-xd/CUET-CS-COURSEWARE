"""
A Python script to simulate the feature of issuing books from a library.
To store the data of books issued by a certain user.
Managing user accounts of library.
Data of available books in the library.
"""


import csv
import datetime
import time

books={}

BorrowDefaulter = "As per our terms and conditions, in case of failing to return a book borrowed from us,\nyou have to pay a fine of 150$ and we shall prohibit your access to our bookstore permanently and blacklist you after cancelling your library subscription provided that no refund will be given from our side under any circumstances."


# To make an account in Accounts.csv
def SignUp (username,user,subscribed,plan,tenure_of_plan,Penalty,Profession):
        with open ("Accounts.csv","r") as file:
            reader=csv.reader(file)
            previousData=[]
            for record in reader:
                if record[0]==username:
                    return "Username exists already, try again!"
                else:
                    previousData.append(record)
            

        with open ("Accounts.csv","w") as file:        
            writer=csv.writer(file,lineterminator="\n",delimiter=",")
            currData=[username,user,subscribed,plan,tenure_of_plan,Penalty,Profession]
            previousData.append(currData)
            writer.writerows(previousData)

# To display the account details of an user, only when he requests to fetch it
def SignIn(username):
    with open("Accounts.csv","r") as file:
        reader=csv.reader(file)
        for record in reader:
            if record[0]==username:
                print("Username: ",record[0])
                print("Subscribed: ",record[1])
                print("Plan: ",record[2])
                print("Tenure of plan: ",record[3])
                print("Penalty: ",record[4])
                print("Profession: ",record[5])
                return 1
        return 0



# To check if a user exists in Accounts.csv or not
def CheckUser(username):
    with open("Accounts.csv","r") as file:
        reader=csv.reader(file)
        for record in reader:
            if record[0]==username:
                return 1
        return 0

#To fetch the price of a requested book (only if the user wants to purchase)
# Currently using this function to fetch the prices of books from AvailableBooks.csv
def FetchPrice(bookName):
    with open ("AvailableBooks.csv","r") as file:
        reader=csv.reader(file)
        for record in reader:
            if record[0]==bookName:
                return record[1]
        return 0

# To search if the library does have the requested book or not
def SearchBook(name,file):
    with open (file,"r") as file:
        reader=csv.reader(file)
        for record in reader:
            if record[0]==name:
                return 1
        return 0

# To push the values of all the keys of a data stored in a dictionary
# Majorly using it for pushing data to IssuedBooks.csv
def Dump(data,file):
    with open(file,"a") as file:
        writer = csv.writer(file,lineterminator="\n",delimiter=",")
        ItemNode = []
        for keys in data:
            ItemNode.append(data[keys])
        writer.writerow(ItemNode)

# Adding a label of "returned when a user has returned a particular book"
def LabellingReturn(username,bookname,file):
    found=False
    with open(file,"r") as file:
        reader = csv.reader(file)
        Data=[]
        # writer = csv.writer(file,lineterminator="\n",delimiter=",")
        for record in reader:
            if record[2]==bookname and record[0]==username:
                found=True
                record[10]="Returned"
                Data.append(record)
            else:
                Data.append(record)

        if found:
            print("We aprreciate your honesty and thanks for visiting.")

        elif not found:
            print("Sorry, we couldn't find this book")
            return 
        
    with open(file,"w") as file:
        writer = csv.writer(file,lineterminator="\n",delimiter=",")
        writer.writerows(data)










"""
_______Marketing___________
To display all the subscirption plans with their respective benefits whenever and wherever I want.

Adding a function to actually let a user to subscribe to any one of the subscription plans he want.
"""

def DisplaySubscriptionPlans():
    print("We have three subscription for all of our users visiting our library.")
    print("\n\n")
    print("1. Basic plan - Free plan for occasional visitors, prohibits users from:")
    print("\n")
    print("- Borrowing any book from us")
    print("- Using their account on multiple devices")
    print("- Using social media and video conferencing while using our interface")
    print("- Accessing study results of institutions and research papers or any high level academic or learning material.")
    
    time.sleep(5)
    print("\n\n")

    print("2. Intermediate - A 2 week plan of 10$ which provides you with: ")
    print("\n")
    print(r"- A discount of 40% on your gross purchase.")
    print("- Our real-time chat software to group study with your friends.")
    print("- Privilege to use your account on maximum three devices, irrespective of the device type.")
    print("- Access to read paid novels, research papers and view study results of top worldwide institutions.")
    
    time.sleep(5)
    print("\n\n")

    print("3. Pro - Monthly plan of 80$ which will get you: ")
    print("\n")
    print("- Privilege to use our AI assitant to get help in solving your homework problems.")
    print("- Access to previous question papers and questions of your board, competitive exams and semester exams.")
    print("- Free access to previous year questions of your university exams.")
    print("- Discount on book sets, research papers, archaelogical bulletins and tech oriented books.")

    time.sleep(5)
    print("\n\n")

    print("4. Premium - 3 month plan of 100$ which offers you: ")
    print("\n")
    print("- Specialised AI assistant to help you study, analyse and summarize research papers and any study material.")
    print("- Thesis.ai which is an AI bot to help you write and proofread your own research papers and thesis.")
    print("- An interface to collaborate with researchers and scientists and SMEs of your field/subject.")
    print(r"- 70% discount on publishing your thesis and research papers in the market and on the internet as well.")



"""
Letting the user to actually subscribe to his favorite plan.

--Putting a stay on these functions, as I don't feel the need to use them for now.
"""

# def DurationFetcher(plan):
#     if plan.lower()=="basic":
#         return "Unlimited"
#     elif plan.lower()=="intermediate":
#         return "14 days"
#     elif plan.lower()=="pro":
#         return "30 days"
#     elif plan.lower()=="premium":
#         return "90 days"
#     else:
#         return "Please select a valid plan."

# def SubscriptionPriceFetcher(plan):
#     if plan.lower()=="basic":
#         return "Free"
#     elif plan.lower()=="intermediate":
#         return "10$"
#     elif plan.lower()=="pro":
#         return "80$"
#     elif plan.lower()=="premium":
#         return "100$"
#     else:
#         return "Please select a valid plan."



"""
x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-xx-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-xx-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x
"""


# Main UI interface for the user:


while True:
    print("1. GET")
    print("2. Return")
    print("3. My account")
    print("4. Subscribe")
    print("5. Exit")

    choice=int(input("Enter your choice: "))
    if choice==1:
        
        TypeOfPurchase = str(input("Borrow or purchase? "))
        

        # Information related to the book 
        user=str(input("Enter your full name: "))
        username = str(input(f"Enter your username: "))
        request = str(input(f"Enter the name of the book you would like to {TypeOfPurchase} from us: "))
        author = str(input(f"Enter the name of the author of this book: "))
        Availability = bool(SearchBook(request,"AvailableBooks.csv"))
        genre=str(input("Genre: "))
        ReturnStatus=""
        price=FetchPrice(request)
        if price==0:
            price=0
        
        condition = author.lower() not in ("","idk") and Availability==True 
        CurrentDate = str(datetime.date.today()).replace("-","/")
        
        if TypeOfPurchase.lower()=="borrow":
            if condition==True:
                UserExists = CheckUser(username)
                if bool(UserExists)==True:
                    pass
                else:
                    # Run sign up function
                    print("Since you don't have an account, you need to make one.")
                    print("Fill the information below to make your account.")
                    plan=str(input("Select a plan: "))
                    profession=str(input("Enter your profession here (Student if none): "))
                    SignUp(username,user,subscribed="No",plan="Basic",tenure_of_plan="Unlimited",Penalty=("None"),Profession=profession)
            
                duration=int(input("For how many days do you want to keep this book with yourself? "))
                fine="150$"
                ReturnStatus="Not yet"
                if duration>14:
                    print("Sorry, we don't lend anyone any book for that much of duration.")
                    continue
                else:
                    print("Ok, you can borrow this book for this duration of time, have a nice day.")
                    print(BorrowDefaulter)
                    price+=0

            else:
                newBook={"Name":request}
                Dump(newBook,"AvailableBooks.csv")
                print("Sorry for the inconvenience but we didn't had this in our library.")
                print("But don't worry, we'll soon fetch it for you, you may check for it in a day or two.")

        elif TypeOfPurchase.lower()=="purchase":
            if condition==True:
                # Print a thank you message and add this account to the CSV file
                print("Thanks for visiting us sir! Have a nice day.")
                UserExists = CheckUser(username)
                if bool(UserExists)==True:
                    pass
                else:
                    # Run sign up function
                    print("Since you don't have an account, you need to make one.")
                    print("Fill the information below to make your account.")
                    profession=str(input("Enter your profession here (Student if none): "))
                    SignUp(username,user,subscribed="No",plan="Basic",tenure_of_plan="Unlimited",Penalty="None",Profession=profession)

                ReturnStatus="N/A"

            else:
                newBook={"Name":request}
                Dump(newBook,"AvailableBooks.csv")
                print("Sorry for the inconvenience but we didn't had this in our library.")
                print("But don't worry, we'll soon fetch it for you, you may check for it in a day or two.")

        if condition==True and price!=0:
            data={
                    "Username":username,
                    "User":user,
                    "Name":request,
                    "Author":author,
                    "Genre":genre,
                    "Type":TypeOfPurchase,
                    "Price":price,
                    "Duration":duration,
                    "Fine":fine,
                    "Date":CurrentDate,
                    "Returned":"Not yet"
            }

            books[username]=data
            Dump(data,"IssuedBooks.csv")
        
        if condition==True and price!=0:
            print("Sorry we can't provide you with this book \n as we haven't decided the post discount price of it.")
        
        elif condition!=True:
            print("Some error occured :(")
            print("Check if you have provided us with the author's name or not.")
            
    elif choice==2:
            username=str(input("Enter your username: "))
            BookToBeReturned = str(input(f"Enter the name of the book that you borrowed from us: "))                    
            LabellingReturn(username,BookToBeReturned,"IssuedBooks.csv")

    elif choice==3:    
        request = str(input(f"Enter your username: "))
        response = SignIn(request)
        if response==0:
            print("Error 404: Account not found.")


    elif choice==4:
        DisplaySubscriptionPlans()
        choice=int(input("Which plan would you like to subcribe to: "))


    elif choice==5:
        break

    else:
        print('Please make a valid choice.')

