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