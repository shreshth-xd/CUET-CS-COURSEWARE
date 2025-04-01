# Reading the content of a file line by line

file=open("sentences.txt","r")
for line in file:
    print(line ,end="")