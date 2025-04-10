# Implementing Bubble sort algorithm in Python
lst=[]
count=int(input("How many elements do you want in the list: "))
for i in range(count):
    item=int(input("Enter the item: "))
    lst.append(item)

n=len(lst)
print("Unsorted list:",lst)

# Logic and explanation of bubble sort algorithm 
"""
In bubble sort algorithm, all we have to do is to start with comparing the starting value of the list with the value
coming after it and swap it as per our sort order (ascending or descending) and the process is repeated till
the list is sorted as per the required sort order.

Basically bubbling the biggest value of the list to the end of the list to sort it in an ascending order. 
The worst case time complexity of Bubble sort algorithm is O(n²) and..
the best case time complexity of this algorithm is O(n), which means that all the elements are sorted already,
when all the elements are sorted in the required order already then all the algorithm has to do is to just
compare the values of the list if they are in the required order or not.
"""


# Code
for i in range(0,n):
    for j in range(0,n-i-1):
        if lst[j]>lst[j+1]:
            lst[j],lst[j+1]=lst[j+1],lst[j]

print("Sorted list:",lst)