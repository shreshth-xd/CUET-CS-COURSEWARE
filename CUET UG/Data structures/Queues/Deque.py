# A Deque stands for double ending queue, which allows the insertion and deletion operation from both the ends

queue=[]
front=0
rear=len(queue)-1


def isEmpty(queue):
    if queue==[]:
        return True
    else:
        return False
    

def enqueue(item,queue):
    if isEmpty(queue):
        front=rear=0
        queue.append(item)
    else:
        queue.append(item)
        rear=len(queue)-1


def dequeue(queue):
    if isEmpty(queue):
        print("Underflow")
    else:
        item=queue.pop(0)
        return item

