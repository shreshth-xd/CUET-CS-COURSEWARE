# A Python script to simulate the feature of issuing books from a library
# To store the data of books issued by a certain user.


import csv
import datetime

books={}

BorrowDefaulter = "As per our terms and conditions, in case of failing to return a book borrowed from us,\nyou have to pay a fine of 150$ and we shall prohibit your access to our bookstore permanently and blacklist you after cancelling your library subscription provided that no refund will be given from our side under any circumstances."


def Dump(data,file):
    with open(file,"a") as file:
        writer = csv.writer(file,lineterminator="\n",delimiter=",")
        ItemNode = []
        for keys in data:
            ItemNode.append(data[keys])
        writer.writerow(ItemNode)


def LabellingReturn(user,bookname,file):
    with open(file,"r+") as file:
        reader = csv.reader(file)
        writer = csv.writer(file,lineterminator="\n",delimiter=",")
        for record in reader:
            if record[1]==bookname and record[0]==user:
                found=True
                record[8]="Returned"
                writer.writerow(record)
                print("We aprreciate your honesty and thanks for visiting.")
                break
            else:
                writer.writerow(record)

        if not found:
            print("Sorry, we couldn't find this book")
            print("")

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
        request = str(input(f"Enter the name of the book you would like to {TypeOfPurchase} from us: "))
        author = str(input(f"Enter the name of the author of this book: "))
        NonAvailability = request not in books
        condition = author.lower()!="" and author.lower()!="idk"
        genre=str(input("Genre: "))
        price=0        
        CurrentDate = str(datetime.date.today()).replace("-","/")
        
        if TypeOfPurchase.lower()=="borrow":
            duration=int(input("For how many days do you want to keep this book with yourself? "))
            if duration>14:
                print("Sorry, we don't lend anyone any book for that much of duration.")
                continue
            else:
                print("Ok, you can borrow this book for this duration of time, have a nice day.")
                print(BorrowDefaulter)
                price+=0

        if condition==True:
            data={
                    "User":user,
                    "Name":request,
                    "Author":author,
                    "Genre":genre,
                    "Type":TypeOfPurchase,
                    "Price":price,
                    "Duration":duration,
                    "Fine":"150$",
                    "Date":CurrentDate,
                    "Returned":"Not yet"
            }

            books[request]=data
            Dump(data,"IssuedBooks.csv")
        
    elif choice==2:
            user=str(input("Enter your name: "))
            BookToBeReturned = str(input(f"Enter the name of the book that you borrowed from us: "))                    
            LabellingReturn(user,BookToBeReturned,"IssuedBooks.csv")

    elif choice==4:
        break

    else:
        print('Please make a valid choice.')

