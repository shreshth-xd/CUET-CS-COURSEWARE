import mysql.connector as connector

con = connector.connect(host="localhost", user="root", password="password", database="test")
if con.is_connected():
    print("Connection with database successful")

cursorObj=con.cursor()
SampleQuery="SELECT * FROM table1;"
cursorObj.execute()
data=cursorObj.fetchall()

for row in data:
    print(row)

con.close()