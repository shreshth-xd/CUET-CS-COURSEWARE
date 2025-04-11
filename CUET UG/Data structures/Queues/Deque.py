# A Deque stands for double ending queue, which allows the insertion and deletion operation from both the ends

queue=[]
front=0
rear=len(queue)-1


def isEmpty(queue):
    if queue==[]:
        return True
    else:
        return False
    
# Normal enqueue as per the FIFO technique
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
    

def peek(queue):
    if isEmpty(queue):
        return "The Queue is empty."
    else:
        item=queue[0]
        return item


# Deque functions:

# Enqueue function to push an element at the front
def l_enqueue(item,queue):
    if isEmpty(queue):
        front=rear=0
        queue.insert(0,item)
    else:
        queue.insert(0,item)
        rear=len(queue)-1



# Deleting an element from the rear end of the queue
def r_dequeue(queue):
    if isEmpty(queue):
        print("Underflow")
    else:
        item=queue.pop()
        return item
    

def peekRight(queue):
    if isEmpty(queue):
        print("The Queue is empty.")
    else:
        rear=len(queue)-1
        item=queue[rear]
        return item