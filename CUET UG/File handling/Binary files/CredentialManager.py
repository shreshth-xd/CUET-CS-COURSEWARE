import pickle
import pyperclip

print("Simple script to store your credentials in an encrypted form in a binary file.")
password=str(input("Enter your password: "))

with open("credentials.dat","ab+") as file:
    pickle.dump(password,file)

copy_password=str(input("Copy password to clipboard: "))
if copy_password.lower()!="no":
    with open("credentials.dat","r") as file:
        password=pickle.load(file)
        print(password)
        print("Password copied to clipboard.")