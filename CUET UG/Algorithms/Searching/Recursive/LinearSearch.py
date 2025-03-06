# Implementing Linear search in Python on a list using recursion
lst=[1,4,6,7,2,3,90,1578,345]
low=0
size=len(lst)
item=int(input("Enter the item to search for: "))

def linearSearch(low,size,item,array):
    if low<size:
        if array[low]==item:
            return low
        else:
            linearSearch(low+1,size,item,array)
    else:
        return 0

index_no = linearSearch(low,size,item,lst)
if index_no==0:
    print("Search unsuccessful.")
    print("Item not found.")
else:
    print(item,"found at index number: ",index_no)