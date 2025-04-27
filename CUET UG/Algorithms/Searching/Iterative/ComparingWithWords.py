wordList=["Perfect", "Stupendous", "Wondrous", "Gorgeous", "Awesome", "Mirthful", "Fabulous", "Splendid", "Incredible", "Outstanding", "Propitious","Remarkable", "Stellar", "Unbelievable", "Super", "Amazing"]

def selectionSort(array,length):
    for i in range(0, length-1):
        min_=array[i]
        for j in range(i+1, length):
            if array[j]<min_:
                min_=j
        
        if min_!=i:
            array[i],array[min_]=array[min_],array[i]
    
    return array

def linearSearch(key,array):
    i=0
    n=len(array)
    while i<n and array[i]!=key:
        i=i+1
    
    else:
        if i<n:
            print(f"{key} found at {i} index.")
        else:
            print("Search unsuccessful.")

def binarySearch(key,array):
    low=0
    high=len(array)-1
    while low<high:
        mid=int((low+high)/2)
        if array[mid]==key:
            return key
        