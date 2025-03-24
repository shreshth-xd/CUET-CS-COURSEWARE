# Implementing Queues in Python using lists

"""
1. Enqueue
2. Dequeue
3. Peek
4. Underflow
"""

queue=[]
front=0
rear=len(queue)-1

def isEmpty(q):
    if q==[]:
        return True
    else:
        return False


def Enqueue(item,q):
    if isEmpty(q):
        q.append(item)
        front=rear=0
    else:
        q.append(item)
        back=len(q)-1
    return 1


def Dequeue(q):
    if isEmpty(q):
        return "Underflow"
    item = q.pop(0)
    return item


def Peek(q):
    if isEmpty(q):
        return "The Queue is empty!"
    return q[0]


def Display(q):
    front=0
    rear=len(q)-1
    print(q[front],"<---- front")
    for i in range(1,len(q)-1):
        print(q[i])
    print(q[rear],"<---- rear")


while True:
    print("1. Peek")
    print("2. Enqueue")
    print("3. Dequeue")
    print("4. Display")
    print("5. Exit")

    request=int(input("Enter your choice: "))

    if request==1:
        response=Peek(queue)
        print(response)        
    
    elif request==2:
        item=int(input("Enter the item you want to push into the Queue: "))
        Enqueue(item,queue)