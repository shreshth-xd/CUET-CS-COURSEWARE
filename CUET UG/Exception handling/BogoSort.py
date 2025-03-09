"""
For those, who don't Bogo sort is also a sorting algorithm which basically takes an array/list and 
keeps on shuffling it until the array is automatically sorted.
"""

import random

lst=[]
n=int(input("Enter the number of items you want: "))
for i in range(n):
    item=int(input("Enter the item: "))
    lst.append(item)


def IsSorted(array):
    for i in range(0,n-1):
        if array[i]>array[i+1]:
            return False
    return True


try:
    chances=int(input("How many chances(no. of shuffles) do you want to give to Bogo sort: "))
    
    for i in range(chances):
        random.shuffle(lst) 
        if IsSorted(lst):
            print(lst)
            break  

    sorted_=IsSorted(lst)
    if sorted_==False:
        raise Exception("Random shuffling didn't do it.")
    
except Exception:
    print("Bogo sort couldn't sort it in",chances,"shuffles.")
else:
    print("Sorted succesfully.")
finally:
    print("I hope you've understood if random actions does make an impact in this universe or not 🍃.")