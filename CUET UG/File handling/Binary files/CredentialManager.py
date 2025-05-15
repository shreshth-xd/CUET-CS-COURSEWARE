import pickle
import pyperclip

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
