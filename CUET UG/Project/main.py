import json
import bcrypt

numbers="0123456789"
letters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

validForusername="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"

def register(username,password):
    try:
        # Only letters, numbers and underscores are allowed in username field
        # The username has to be unique
        while True:
            username=str(input("Enter the username: "))
            if validForusername not in username:
                raise Exception("Only letters, numbers and underscore is permissable for username.")
            else:
                break
    except Exception as e:
        print("Exception occurred: ",e)


def login(username,password):
    try:
    # Only letters, numbers and underscores are allowed in username field
    # The username has to be unique
        pass
    except NameError:
        # To be continued
        pass


def change_password(username,password):
    try:
        # Only letters, numbers and underscores are allowed in username field
        # The username has to be unique
        pass
    except NameError:
        # To be continued
        pass