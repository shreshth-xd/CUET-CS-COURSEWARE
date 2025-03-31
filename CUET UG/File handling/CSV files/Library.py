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

# To display the account details of an user, only when he requests to fetch it
# def SignIn(user,file)

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

def SubscriptionPlans():
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




while True:
    print("1. GET")
    print("2. Return")
    print("3. My account")
    print("4. Exit")

    choice=int(input("Enter your choice: "))
    if choice==1:
        
        TypeOfPurchase = str(input("Borrow or purchase? "))
        
        # User information:
        user=str(input("Enter your full name: "))

        # Information related to the book
        username = str(input(f"Enter your username: "))
        request = str(input(f"Enter the name of the book you would like to {TypeOfPurchase} from us: "))
        author = str(input(f"Enter the name of the author of this book: "))
        Availability = bool(SearchBook(request,"AvailableBooks.csv"))
        condition = author.lower()!="" and author.lower()!="idk" and Availability==True
        genre=str(input("Genre: "))
        price=FetchPrice(request)
        if price==0:
            price=0

        CurrentDate = str(datetime.date.today()).replace("-","/")
        
        if TypeOfPurchase.lower()=="borrow":
            duration=int(input("For how many days do you want to keep this book with yourself? "))
            fine="150$"
            if duration>14:
                print("Sorry, we don't lend anyone any book for that much of duration.")
                continue
            else:
                print("Ok, you can borrow this book for this duration of time, have a nice day.")
                print(BorrowDefaulter)
                price+=0
        
        elif TypeOfPurchase.lower()=="purchase":
            if condition==True:
                # Print a thank you message and add this book to the user's account
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

            else:
                newBook={"Name":request}
                Dump(newBook,"AvailableBooks.csv")
                print("Sorry for the inconvenience but we didn't had this in our library.")
                print("But don't worry, we'll soon fetch it for you, you may check for it in a day or two.")

        if condition==True:
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
        
    elif choice==2:
            username=str(input("Enter your username: "))
            BookToBeReturned = str(input(f"Enter the name of the book that you borrowed from us: "))                    
            LabellingReturn(username,BookToBeReturned,"IssuedBooks.csv")

    # elif choice==3:    

    elif choice==4:
        break

    else:
        print('Please make a valid choice.')

