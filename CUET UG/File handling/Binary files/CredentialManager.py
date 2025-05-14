import pickle
import pyperclip

print("Simple script to store your credentials in an encrypted form in a binary file.")
password=str(input("Enter your password: "))

with open("credentials.dat","ab+"):
    pickle.dump(password,"credentials.dat")

