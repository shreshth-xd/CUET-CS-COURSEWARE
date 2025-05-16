import pickle
import pyperclip
import time

print("This program is for just revising how text is serialised and pushed into a binary file.\n")
print("Apparently, binary files are not a good choice for storing credentials and especially passwords.\n")
print("I advise you guys to push some sample password to your respective credentials.dat files\nand see if it actually protects your credentials or not.")
time.sleep(4)
print("Simple script to store your credentials in an encrypted form in a binary file.")
password=str(input("Enter your password: "))

with open("credentials.dat","wb") as file:
    pickle.dump(password,file)

copy_password=str(input("Copy password to clipboard: "))
if copy_password.lower()!="no":
    with open(r'credentials.dat',"rb") as file:
        password=pickle.load(file)
        pyperclip.copy(password)
        print("Password copied to clipboard.")
else:
    pass

