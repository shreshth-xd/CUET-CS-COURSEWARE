# Implementing Insertion sort algorithm in Python

lst=[]
count=int(input("Enter the number of items: "))
for i in range(count):
    item=int(input("Enter the item: "))
    lst.append(item)
n=len(lst)
print("Unsorted array: ",lst)
"""
In Insertion sort algorithm, we start with the comparing the second element i.e. the element at the index
number 1, with the element precceding it and then we swap both of these elements as per our sort order(ascending
or descending), then this process of comparing the current element with it's precedding one and swapping them is
repeated until the array is sorted.

The worst case time complexity of Insertion sort algorithm is O(n²) and..
the best case time complexity of this algorithm is O(n), which means that all the elements are sorted already
"""


# Logic:
# Using the curr variable to access the the element to be compared
# Initialising j so as to access the index of the precedding element.
for i in range(1,n):
    curr=lst[i]
    j=i-1
    while j>=0 and curr<lst[j]:
        lst[j+1]=lst[j]
    else:
        lst[j+1]=curr
print("Sorted array: ",lst)