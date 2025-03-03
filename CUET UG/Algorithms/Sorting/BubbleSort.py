# Implementing Bubble sort algorithm in Python
array=[]
count=int(input("How many elements do you want in the array: "))
for i in range(count):
    item=int(input("Enter the item: "))
    array.append(item)

n=len(array)
print("Unsorted array: ",array)
"""
In bubble sort algorithm, all we have to do is to compare the starting value of the array with the value
coming after it and swap it as per our sort order (ascending or descending) and the process is repeated till
the array is sorted as per the required sort order.

Basically bubbling the biggest value of the array to the end of the array to sort it in an ascending order. 
"""

for i in range(0,n):
    for j in range(0,n-i-1):
        if array[j]>array[j+1]:
            array[j],array[j+1] = array[j+1],array[j]


print("Sorted array: ",array)