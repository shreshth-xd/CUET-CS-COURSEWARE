lst=[5,6,7,8,9,10]
low=0
high=len(lst)

def BinarySearch(low,high,item,array):
    mid=int((low+high)/2)
    if low<high:        
        if item==array[mid]:
            return mid
        elif item>array[mid]:
            low=mid+1
            BinarySearch(low,high,item,array)
        elif item<array[mid]:
            high=mid-1
            BinarySearch(low,high,item,array)
    else:
        return 0

search_item = int(input("Enter the item to search for: "))
index=BinarySearch(low,high,search_item,lst)
if index==0:
    print("Search unsuccessful.")
    print("Item not found.")
else:
    print(search_item,"found at index number",index)