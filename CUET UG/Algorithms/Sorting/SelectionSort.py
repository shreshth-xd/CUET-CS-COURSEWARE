# Implementing Selection sort algorithm in Python

lst=[]
count=int(input("Enter the number of elements: "))
for i in range(count):
    item=int(input('Enter the item: '))
    lst.append(item)

n=len(lst)
print("Unsorted list: ",lst)


""""
When it comes to implementation and time complexity, selection sort may seems similar to insertion sort,
however, unlike insertion sort what we do here is to assume the 1st element(index number 0) to be 
the minimum/maximum element and then we keep on moving our loop counter alongwith checkin
for a value which is smaller/larger than the initially assumed minimum/maximum element,
and when we encounter such an element, then only we swap these two element i.e. swapping the
assumed minimum/maximum  element with the newly scanned minimum/maximum value after that particular iteration. 
"""


# Logic:
"""
Initialising the i variable of the loop with 0 so as to access the first element of the list in the 1st 
iteration and assuming it to be the minimum element by assigning the value of i to be "min_" variable
, the outer loop is being traversed from 0 to n-1 so as to access those elements with whom we are going to 
compare the elements in our inner loop which is traversed from i+1 to n.


In the inner loop, we check for a number which possibly more smaller than the assumed smallest number and
updating it's index with every passing iteration as long as that iteration's control goes to the if block 
i.e. if the condition in our if block results to true. 


With each passing iteration of the inner loop our "min_" variable is being updated and 
after the termination of this inner loop the control goes to the if condition block which 
is the part of the outer loop. 

In which the actual minimum element is swapped with the pre-assumed smallest element and the
pre-assumed smallest element is shifted to it's correct and actual position due to this swapping.

The same above process is repeated for all the i'th elements in the array/list till the termination of outer loop
"""

for i in range(0,n-1):
    min_=i
    for j in range(i+1,n):
        if lst[j]<lst[min_]:
            min_=j
    
    if min_!=i:
        lst[i],lst[min_]=lst[min_],lst[i]
        
print("Sorted list: ",lst)