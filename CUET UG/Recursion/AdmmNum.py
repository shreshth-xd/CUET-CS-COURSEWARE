"""
In this program we have a list which contains admission numbers of n number of students sorted in ascending
order, after which user serches for a student through his/her admission number and we'll look for it
using recursive binary search.
"""

record = [01,02,03,04,05,06,07,08,09,10]
number = int(input('Enter the admission number of your student: '))
low=0
high=len(record)


def BinarySearch(low,high,item,array):
    if low<high:
        mid = int((low+high)/2)
        if array[mid]==item:
            return 1
        elif array[mid]<item:
            low=mid+1
            BinarySearch(low,high,item,array)
        elif array[mid]>item:
            high=mid-1
            BinarySearch(low,high,item,array)
    else:
        return 0
response=BinarySearch(low,high,number,record)
if response==1:
    print("Search successfull, we do have this admission number in our record.")
else:
    print("Search successfull, we do not have this admission number in our record.")