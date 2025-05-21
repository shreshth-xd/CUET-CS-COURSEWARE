import mysql.connector as connector

con = connector.connect(host="localhost", user="root", password="password", database="test")
if con.is_connected():
    print("Connection with database successful")