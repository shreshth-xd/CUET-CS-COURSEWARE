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
    sorted=IsSorted(lst)
except not sorted:
    print("Bogo sort couldn't sort it in",chances,"shuffles.")
