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

def Peek(q):
    if isEmpty(q):
        return "The Queue is empty!"
    return q[0]