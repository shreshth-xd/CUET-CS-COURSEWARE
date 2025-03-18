import json
import bcrypt
import re

# Regex pattern to enusre that the password contains numbers and special symbols along with letters
pattern = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*\W)[A-Za-z\d\W]{8,}$'


def get_hash(password,round=12):
    # Generating a salt to be included in the hashed password 
    salt=bcrypt.gensalt(rounds=round)    
    password_bytes = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(password_bytes,salt)
    return hashed_password

def register(username,password):
    try:
        # Only letters, numbers and underscores are allowed in username field
        # The username has to be unique        

        
        # The regex pattern "\w+" ensures that the username has only letters, numbers and underscores
        # Since the fullmatch() and match() methods of re returns an object, I have typecasted it into a bool

        with open ("test.json","r") as file:
            existing_data = json.load(file)
            for key in existing_data.keys():
                if username==key:
                    raise NameError
            pass

        if bool(re.fullmatch(r"\w+",username))==False:
            raise ValueError
        if bool(re.match(pattern,password))==False:
            raise KeyError
        else:

            # Decoding the bytes returned by the getHash function, since JSON module does not allows
            # bytes to be dumped into a JSON file
            hashed_password = get_hash(password).decode(encoding='utf-8')  
            data = {
                "username":username,
                "password":hashed_password
            }

            try:
                with open ("test.json","r") as file:
                    existing_data = json.load(file)
            except (FileNotFoundError, json.JSONDecodeError):
                existing_data={}


            with open("test.json","w") as file:
                if username not in existing_data:
                    existing_data[username] = data
                    json.dump(existing_data,file,indent=4)

    except ValueError:
        print("Only letters, numbers and underscore is permissable for username.")
        return "Invalid username"
    except KeyError:
        print("Your password is not strong.")
        return "Invalid password"
    except NameError:
        print("Username is not unavailable")
        return "Unavailable username"  

def login(username, password_):    
    with open("test.json", "r") as file:
        existing_data = json.load(file)
    
    if username not in existing_data:
        return "Invalid username or password"
    
    stored_hashed_password = existing_data[username]["password"].encode("utf-8")  # Retrieve stored hash
    
    # Correct way to verify password
    if bcrypt.checkpw(password_.encode("utf-8"), stored_hashed_password):
        print("Login successful!")
        print("Welcome to the system, sir!")
    else:
        return "Invalid username or password"


def change_password(username,password,new_password):

    try:
        with open('test.json','r') as file:
            existing_data = json.load(file)
        
            if username not in existing_data:
                return "Illegitimate user"

            if bool(re.match(pattern,new_password))==False:
                return "Your password is not strong"

            stored_hashed_password = existing_data[username]["password"].encode('utf-8')
            if not bcrypt.checkpw(password.encode('utf-8'),stored_hashed_password):
                return "Illegitimate user"
            
            hashed_new_password = get_hash(new_password).decode('utf-8')
            existing_data[username]["password"] = hashed_new_password

            with open("test.json","w") as file:
                json.dump(existing_data,file)
                return "Password changed succesfully"

    except (FileNotFoundError, json.JSONDecodeError):
        return "Err: User's database is corrupted or missing"
    

def change_username(username,password,new_username):
    try:
        with open("test.json","r") as file:
            existing_data=json.load(file)
        
            if username not in existing_data:
                return "Illegitimate user"
        
            stored_hashed_password = existing_data[username]["password"].encode('utf-8')
            if not bcrypt.checkpw(password.encode('utf-8'),stored_hashed_password):
                return "Illegitimate user"

            if new_username in existing_data:
                return "Unavailable username"
        
            existing_data[new_username]=existing_data.pop(username)
            existing_data[new_username]["username"]=new_username

        with open ("test.json","w") as file:
            json.dump(existing_data,file,indent=4)
            return "Username changed succesfully"
        

    except (FileNotFoundError, json.JSONDecodeError):
        return "Error: User database corrupted or missing"

while True:
    print("1. Register")
    print("2. Login")
    print("3. Change password")
    print("4. Change username")
    print("5. Exit")
    choice=int(input(">"))
    if choice==1:
        while True:
            username=str(input("Enter the username: "))
            password=str(input("Enter your password: "))
            response = register(username,password)

            if response=="Invalid username" or response=="Invalid password" or response=="Unavailable username":
                print("Try to register yourself again.")
            else:
                break

    elif choice==2:
        i=0
        while True:
            username=str(input("Enter your username: "))
            password=str(input("Enter your password: "))
            response=login(username,password)
            if i>4:
                print("We have detected some suspicious activities from your side.")
                print("We are not permitting you to carry out this operation anymore.")
                break
            if response=="Invalid username or password":
                print("Invalid username or password")
                print("Try logging in again.")
                i+=1
            else:
                i=0
                break
    
    elif choice==3:
        i=0
        while True:
            username=str(input("Enter your username: "))
            password=str(input("Enter your old password: "))
            new_password=str(input("Enter your new password: "))
            response=change_password(username,password,new_password)
            if i>4:
                print("We have detected some suspicious activities from your side.")
                print("We are not permitting you to carry out this operation anymore.")
                break
            if response=="Illegitimate user":
                print("The username or password that you've entered is wrong!")
                print("Try again!")
                i+=1
            elif response=="Password changed succesfully":
                i=0
                print("Password changed successfully.")
                break

            elif response=="Your password is not strong":
                print(response)
                print("Choose a more strong and unguessable password")
    
    elif choice==4:
        i=0
        while True:
            username=str(input("Enter your old username: "))
            password=str(input("Enter your password: "))
            new_username = str(input("Enter your new username: "))
            response=change_username(username,password,new_username)
            
            if i>4:
                print("We have detected some suspicious activities from your side.")
                print("We are not permitting you to carry out this operation anymore.")
                break
            if response=="Unavailable username":
                print("Try again!")
            if response=="Illegitimate user":
                print("The username or password that you've entered is wrong!")
                print("Try again!")
                i+=1
            elif response=="Username changed succesfully":
                print("Username changed successfully.")
                break

    elif choice==5:
        break