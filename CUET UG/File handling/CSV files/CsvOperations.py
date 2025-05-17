# To use a sample csv file to see how we can interact with CSV data from a Python script
import csv

# Since the CSV files are read row by row in CSV module, it's not necessary to use try-except or with clause to tackle the EOFError
file=open("Sample.csv","r")
reader=csv.reader(file,delimiter=",")
rows=[row for row in reader]
for i in range(1,len(rows)):
    print(rows[i])