# __name__==__main__ 
# Main script for the Data Analyzer and probability calculator project
# This analyzer currently works only for the purpose of analyzing the performance of students of a class
# Currently using and relying on CSV for data storage
import mysql.connector as connector
import matplotlib.pyplot as plt
import os
from collections import Counter
from dotenv import load_dotenv


def barGraphGenerator(names,averages):
    plt.bar(names,averages)
    plt.title("Overall performance of all students")
    plt.xlabel("Names")
    plt.ylabel("Averages")
    save=str(input("Do you want to save the upcoming graph?"))
    
    if save.lower()=="yes":
        GraphName=str(input("Name: "))
        print("Save it in: ")
        print("1. pdf")
        print("2. docx")
        print("3. png")
        print("4. jpeg")
        print("5. svg")
        format_=str(input(">"))
        plt.savefig(f"Export/{GraphName}.{format_.lower()}")
        plt.show()

    else:
        plt.show()

def lineGraphGenerator(names,averages):
    plt.bar(names,averages)
    plt.title("Overall performance of all students")
    plt.xlabel("Names")
    plt.ylabel("Averages")
    save=str(input("Do you want to save the upcoming graph?"))
    
    if save.lower()=="yes":
        GraphName=str(input("Name: "))
        print("Save it in: ")
        print("1. pdf")
        print("2. docx")
        print("3. png")
        print("4. jpeg")
        print("5. svg")
        format_=str(input(">"))
        plt.savefig(f"Export/{GraphName}.{format_.lower()}")
        plt.show()
    
    else:
        plt.show()



load_dotenv()
conn = connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),  
    database=os.getenv("DB_NAME"))

# Checking if credentials are loaded properly or not
RequiredCreds = ["DB_HOST","DB_USER","DB_PASSWORD","DB_NAME"]
missing = [cred for cred in RequiredCreds if not os.getenv(cred)]

if missing:
    print("Some of your credentials are missing.")
    print(f"Missing env variables: {', '.join(missing)}")

if conn.is_connected():
    print("BASENCE\n")
    print("One stop solution for performance analysis")

# Cursor
Cursor = conn.cursor()

while True:
    print("1. Upload dataset")
    print("2. Update dataset")
    print("3. Project averages")
    print("4. Calculate probability")
    print("5. Exit")
    choice=int(input(">"))
    if choice==1:
        
        # Fetching the table name
        stream = str(input("Enter the stream: "))
        Class_ = str(input("Enter the class of this stream: "))
        strengthOfClass = int(input("Enter the number of students in this class: "))
        
        for i in range(strengthOfClass):
            name=str(input("Enter the name of the student: "))
            if stream.lower()=="pcm":
                print("Write N/A for the elective which has not been chosen by a student.")
                MathScore = int(input("Enter the Mathematics score of the student: "))
                PhysicsScore = int(input("Enter the Physics score of the student: "))
                ChemistryScore = int(input("Enter the Chemistry score of the student: "))
                EnglishScore = int(input("Enter the English score of the student: "))

                # Electives
                print("The following subjects are electives")
                ComputerScienceScore = str(input("Enter the Computer science score of the student: "))
                PhysicalEducationScore = str(input("Enter the Physical score of the student: "))
                
                query = f"insert into pcm values({name},{Class_},{EnglishScore},{PhysicsScore},{ChemistryScore},{MathScore},{ComputerScienceScore},{PhysicalEducationScore})"
                Cursor.execute(query)
            
            elif stream.lower()=="pcb":
                print("Write N/A for the elective which has not been chosen by a student.")
                BioScore = int(input("Enter the Biology score of the student: "))
                PhysicsScore = int(input("Enter the Physics score of the student: "))
                ChemistryScore = int(input("Enter the Chemistry score of the student: "))
                EnglishScore = int(input("Enter the English score of the student: "))

                # Electives
                print("The following subjects are electives")
                ComputerScienceScore = str(input("Enter the Computer science score of the student: "))
                PhysicalEducationScore = str(input("Enter the Physical score of the student: "))
                
                query = f"insert into pcb values({name},{Class_},{EnglishScore},{PhysicsScore},{ChemistryScore},{BioScore},{ComputerScienceScore},{PhysicalEducationScore})"
                Cursor.execute(query)
            
            elif stream.lower()=="commerce":
                print("Write N/A for the elective which has not been chosen by a student.")
                EnglishScore = int(input("Enter the English score of the student: "))
                AccountancyScore = int(input("Enter the Biology score of the student: "))
                BusinessStudiesScore = int(input("Enter the Physics score of the student: "))
                EconomicsScore = int(input("Enter the Chemistry score of the student: "))

                # Electives
                print("The following subjects are electives")
                ComputerScienceScore = str(input("Enter the Computer science score of the student: "))
                PhysicalEducationScore = str(input("Enter the Physical score of the student: "))

                query = f"insert into pcb values({name},{Class_},{EnglishScore},{AccountancyScore},{BusinessStudiesScore},{EconomicsScore},{ComputerScienceScore},{PhysicalEducationScore})"
                Cursor.execute(query)

    elif choice==2:
        print("DISCLAIMER:")
        print("Update dataset only allows you to update the marks of the already present students in the database.")
        table=str(input("Stream: "))


    elif choice==3:
        names=[]
        averages=[]

        table=str(input("Stream: "))
        query=f"select name, (English+Physics+Chemistry+Maths+round(floor(computer_science),1)+round(floor(computer_science),1))/6 as average from {table.lower()};"
        
        Cursor.execute(query)
        data=Cursor.fetchall()

        for row in data:
            names.append(row[0])
            averages.append(row[1])
        
        graphChoice=str(input("Do you want a line graph or a bar graph? "))
        if graphChoice.lower()=="line":
            lineGraphGenerator(names,averages)
        elif graphChoice.lower()=="bar":
            barGraphGenerator(names,averages)

    elif choice==4:
        # To calculate the probability of a selected student to have a particular average
        averages=[]
        probabilities=[]
        table=str(input("Stream: "))
        QueryForAverage=f"select (English+Physics+Chemistry+Maths+round(floor(computer_science),1)+round(floor(computer_science),1))/6 as average from {table.lower()};"
        Cursor.execute(QueryForAverage)
        RetreivedAverages=Cursor.fetchall()
        for row in RetreivedAverages:
            averages.append(row[0])

        print(averages)
        favourableAverage=float(input("Favourable average: "))

        probabilityOfEvent=averages.count(favourableAverage)/len(averages)
        print(f"Probability of {favourableAverage} is {probabilityOfEvent}")

        GraphRequest=str(input("Do you want to plot these probabilities on a graph?"))
        if GraphRequest.lower()=="yes":            
            # Storing the probabilities of respective averages
            for item in averages:
                probabilityOfItem=averages.count(item)/len(averages)
                probabilities.append(probabilityOfItem)

            GraphType=str(input("Do you want to plot it on a bar graph or a line graph?"))
            if GraphType.lower() in ("bar","bar graph"):
                barGraphGenerator(averages,probabilities)

            elif GraphType.lower() in ("line","line graph"):
                lineGraphGenerator(averages,probabilities)
        
        else:
            print("")

    elif choice==5:
        break
    else:
        print("Please make a valid choice.")

