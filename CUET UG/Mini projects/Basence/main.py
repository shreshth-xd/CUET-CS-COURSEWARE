# __name__==__main__ 
# Main script for the Data Analyzer and probability calculator project
# This analyzer currently works only for the purpose of analyzing the performance of students of a class
# Currently using and relying on CSV for data storage
import mysql.connector as connector
import matplotlib.pyplot as plt
import os
from matplotlib.ticker import MultipleLocator
from dotenv import load_dotenv


# To plot a bar graph whose x and y axes along with it's respective labels are given 
def barGraphGenerator(x,y,XLABEL,YLABEL,title):
    plt.figure(figsize=(20,14))
    plt.bar(x,y)
    
    # Getting current axis
    ax=plt.gca()
    # Setting locator to the x axis and y axis so that it shows the values coming between two discrete integers
    
    ax.xaxis.set_major_locator(MultipleLocator(1))
    
    plt.title(f"{title}")
    plt.xticks(rotation=45, ha="right")
    plt.xlabel(f"{XLABEL}")
    plt.ylabel(f"{YLABEL}")
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
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    else:
        plt.show()


# To plot a line graph whose x and y axes along with it's respective labels are given 
def lineGraphGenerator(x,y,XLABEL,YLABEL,title):
    
    # Adjusting the size of graph so as to prevent it from collapsing in case of lot of values on x axis
    plt.figure(figsize=(12,6))
    plt.plot(x,y,marker="o")
    
    # Getting current axis
    ax=plt.gca()
    # Setting locator to the x axis and y axis so that it shows the values coming between two discrete integers
    
    ax.xaxis.set_major_locator(MultipleLocator(1))
    
    plt.title(f"{title}")
    plt.xticks(rotation=45,ha="right")
    plt.xlabel(f"{XLABEL}")
    plt.ylabel(f"{YLABEL}")
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
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    
    else:
        plt.show()


def UpdateRecord(table):
    if ("pcm") in table.lower():
        name=str(input("Enter the name of the student: "))
        class_=str(input("Enter the class: "))
        subject=str(input("Enter the subject: "))
        marks=int(input("Enter the new marks of this student: "))
        query=f'update pcm set {subject}={marks} where name="{name.lower()}";'
        Cursor.execute(query)
        
    elif ("commerce") in table.lower():
        name=str(input("Enter the name of the student: "))
        class_=str(input("Enter the class: "))
        subject=str(input("Enter the subject: "))
        marks=int(input("Enter the new marks of this student: "))
        query=f"update pcm set {subject.lower()}={marks} where name={name.lower()}"
        Cursor.execute(query)
        
    elif ("pcb") in table.lower():
        name=str(input("Enter the name of the student: "))
        class_=str(input("Enter the class: "))
        subject=str(input("Enter the subject: "))
        marks=int(input("Enter the new marks of this student: "))
        query=f"update pcm set {subject.lower()}={marks} where name={name.lower()}"
        Cursor.execute(query)
        

    else:
        print("Not a valid stream.")


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
    print("\n\n")
    print("BASENCE:",end="")
    print("One stop solution for performance analysis")

# Cursor
Cursor = conn.cursor()

while True:
    print("1. Upload dataset")
    print("2. Update dataset")
    print("3. Project averages")
    print("4. Calculate probability")
    print("5. Load dataset")
    print("6. Exit")
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
        print("DISCLAIMER:",end="")
        print(" Update dataset only allows you to update the marks of the already present students in the database.")
        table=str(input("Stream: "))
        RecordCount=int(input("Enter how many records do you want to edit: "))
        for i in range(RecordCount):
            UpdateRecord(table)

    elif choice==3:
        names=[]
        averages=[]

        table=str(input("Stream: "))
        if "pcm" in table.lower():
            query=f"select name, (English+Physics+Chemistry+Maths+round(floor(computer_science),1)+round(floor(computer_science),1))/6 as average from {table.lower()};"

        elif "pcb" in table.lower():
            query=f"select name, (English+Physics+Chemistry+Biology+round(floor(computer_science),1)+round(floor(computer_science),1))/6 as average from {table.lower()};"
        
        elif "commerce" in table.lower():
            query=f"select name, (English+Accountancy+Business_studies+Economics+round(floor(computer_science),1)+round(floor(computer_science),1))/6 as average from {table.lower()};"
        
        Cursor.execute(query)
        data=Cursor.fetchall()

        for row in data:
            names.append(row[0])
            averages.append(row[1])
        
        title=str(input("Enter the title of the graph: "))
        graphChoice=str(input("Do you want a line graph or a bar graph? "))
        if graphChoice.lower() in ("line","line graph"):
            lineGraphGenerator(names,averages,"Names","Averages",title)
        elif graphChoice.lower() in ("bar","bar graph"):
            barGraphGenerator(names,averages,"Names","Averages",title)

    elif choice==4:

        # To calculate the probability of a randomly selected student to have a particular average
        averages=[]
        probabilities=[]
        table=str(input("Stream: "))
        if "pcm" in table.lower():
            QueryForAverage=f"select (English+Physics+Chemistry+Maths+round(floor(computer_science),1)+round(floor(computer_science),1))/6 as average from {table.lower()};"

        elif "pcb" in table.lower():
            QueryForAverage=f"select (English+Physics+Chemistry+Biology+round(floor(computer_science),1)+round(floor(computer_science),1))/6 as average from {table.lower()};"
        
        elif "commerce" in table.lower():
            QueryForAverage=f"select (English+Accountancy+Business_studies+Economics+round(floor(computer_science),1)+round(floor(computer_science),1))/6 as average from {table.lower()};"
        

        Cursor.execute(QueryForAverage)
        RetreivedAverages=Cursor.fetchall()
        for row in RetreivedAverages:
            averages.append(int(row[0]))

        # Making a set out of the averages list, so as to plot the probabilities of unique averages only
        uniqueAverages = sorted(set(averages))

        print("Here is the list of all averages of your class:")
        print(uniqueAverages)
        favourableAverage=float(input("Favourable average: "))

        probabilityOfEvent=averages.count(favourableAverage)/len(averages)
        print(f"Probability of {favourableAverage} is {probabilityOfEvent}")

        GraphRequest=str(input("Do you want to plot these probabilities on a graph?"))
        if GraphRequest.lower()=="yes":
                        
            # Storing the probabilities of respective averages
            for item in uniqueAverages:
                probabilityOfItem=averages.count(item)/len(averages)
                probabilities.append(probabilityOfItem)

            title=str(input("Enter the title of this graph: "))
            GraphType=str(input("Do you want to plot it on a bar graph or a line graph?"))
            if GraphType.lower() in ("bar","bar graph"):
                barGraphGenerator(uniqueAverages,probabilities,"Averages","Probabilities",title)

            elif GraphType.lower() in ("line","line graph"):
                lineGraphGenerator(uniqueAverages,probabilities,"Averages","Probabilities",title)
        
        else:
            # Exit with no traces
            pass
    
    elif choice==5:
        # To display the fetched record of a particular student from the relational database
        table=str(input("Enter the stream: "))
        student_id=int(input("Enter the student id of the student: "))
        name=str(input("Enter the name of the student: "))

        query=f'Select * from {table.lower()} where student_ID={student_id} and name="{name}";'
        Cursor.execute(query)
        data=Cursor.fetchall()
        if table.lower()=="pcm":
            attributeSet=("Student ID","Name","Class","English","Physics","Chemistry","Maths","Computer science","Physical education")
            print(attributeSet)
        elif table.lower()=="commerce":
            attributeSet=("Student ID","Name","Class","English","Accountancy","Business studies","Economics","Computer science","Physical education")
            print(attributeSet)
        elif table.lower()=="pcb":
            attributeSet=("Student ID","Name","Class","English","Physics","Chemistry","Biology","Computer science","Physical education")
            print(attributeSet)
        
        for row in data:
            # To print the retrieved query from the result set
            print(row)

    elif choice==6:
        break
    else:
        print("Please make a valid choice.")

conn.commit()
Cursor.close()
conn.close()