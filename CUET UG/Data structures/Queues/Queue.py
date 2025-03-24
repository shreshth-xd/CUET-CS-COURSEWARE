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