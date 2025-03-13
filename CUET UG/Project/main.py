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
# def login(username,password):
#     try:
#     # Only letters, numbers and underscores are allowed in username field
#     # The username has to be unique
        
#     except NameError:
    

# def change_password(username,password):
#     try:
#         # Only letters, numbers and underscores are allowed in username field
#         # The username has to be unique

#     except NameError:

while True:
    print("1. Register")
    print("2. Login")
    print("3. Change password")
    print("4. Exit")
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
        
    elif choice==4:
        break