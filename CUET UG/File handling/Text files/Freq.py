# Making a program in Python to find the word with highest frequency in a text file
# I have made a text file named Temp.txt to store random Latin sentences as content


"""
Using the "with open" method as the opening the file through exception handling and printing the word
with the highest frequency in the "except EOFError" doesn't prints it on the terminal as we are reading
the entire file at once at the starting of this program.
"""
with open('Temp.txt','r') as file:

    content = file.read()
    words = content.split()
    wordFreq = []
    highestFreq = 0
    
    #Storing the word with the highest frequency in this variable
    TopWord=''
    existing=[]
    for word in words:
        count = words.count(word)
        if word not in existing:
            existing.append(word)
            wordFreq.append([word,count])
        if count>highestFreq:
            highestFreq=count
            TopWord = word

    print("The word with the highest frequency is",TopWord,"which has occured",highestFreq,"times.")
    print("The frequency of the all the words are: ",wordFreq)
    print("Hello again")
