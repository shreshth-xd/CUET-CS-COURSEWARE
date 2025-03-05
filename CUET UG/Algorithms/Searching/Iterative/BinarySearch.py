lst=[1,2,3,4,5,6,7]
# n=len(lst)
low=0
high=len(lst)
mid=int((low+high)/2)

item=int(input("Enter the item to search for: "))
while low<high:
    if lst[mid]==item:
        print("Search successful")
        print(item,"found at index number",mid)
    elif item>lst[mid]:
        low=mid+1
    elif item<lst[mid]:
        high=mid-1
else:
    print("Search unsuccessful, item not found.")
    