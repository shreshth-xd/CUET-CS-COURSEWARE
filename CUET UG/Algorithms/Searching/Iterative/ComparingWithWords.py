wordList=["Perfect", "Stupendous", "Wondrous", "Gorgeous", "Awesome", "Mirthful", "Fabulous", "Splendid", "Incredible", "Outstanding", "Propitious","Remarkable", "Stellar", "Unbelievable", "Super", "Amazing"]

def insertionSort(array):
    n=len(array)
    for i in range(1,n):
        curr=array[i]
        j=i-1
        while j>=0 and curr<array[j]:
            array[j+1]=array[j]
            j=j-1
        else:
            array[j+1]=curr

    return array

def selectionSort(array,length):
    for i in range(0, length-1):
        min_=i
        for j in range(i+1, length):
            if array[j]<array[min_]:
                min_=j
        
        if min_!=i:
            array[i],array[min_]=array[min_],array[i]
    
    return array

def bubbleSort(array):
    n=len(array)
    for i in range(0,n):
        for j in range(0,n-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
    
    return array

def linearSearch(key,array):
    i=0
    n=len(array)
    while i<n and array[i]!=key:
        i=i+1

    else:
        if i<n:
            print(f"{key} found after {i} iterations.")
        else:
            print("Search unsuccessful.")

def binarySearch(key,array):
    low=0
    high=len(array)
    comparisions=0
    while low<high:
        comparisions+=1
        mid=int((low+high)/2)
        if array[mid]==key:
            print(f"{key} found after {comparisions} number of comparisions.")
            return key
        elif array[mid]>key:
            high=mid-1
            continue
        else:
            low=mid+1
            continue
    else:
        print("Search unsuccessful.")

word=input("Enter the word to search for in the list: ")
linearSearch(word,wordList)
chooseAlgorithm=str(input("Which algorithm do you want to use to sort this wordlist: "))
if chooseAlgorithm.lower() in ("selection sort","selection"):
    selectionSort(wordList,len(wordList))
elif chooseAlgorithm.lower() in ("bubble sort","bubble"):
    bubbleSort(wordList)
elif chooseAlgorithm.lower() in ("insertion sort","insertion"):
    insertionSort(wordList)

print(wordList)
# print("Finding the word after sorting the list: ")
# linearSearch(word,wordList)
binarySearch(word,wordList)