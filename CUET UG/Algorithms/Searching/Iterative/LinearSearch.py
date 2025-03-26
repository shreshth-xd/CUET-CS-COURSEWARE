# Implementing Linear/Sequential search on a list in Python

lst=[]
count=int(input("Enter the number of elements: "))
for i in range(count):
    item=int(input("Enter the item: "))
    lst.append(item)

n=len(lst)
i=0

search_item = int(input("Enter the item to search for: "))
while i<n and lst[i]!=search_item:
    i+=1

if i<n:
    print(search_item,"found at index number: ",i)
else:
    print("Search unsuccessful.")
    