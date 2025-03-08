# Implementing Stacks in Python using lists

lst=[]
top=None
def isEmpty(stk):
    if stk==[]:
        return True
    else:
        return False

def Push(item,stk):
    stk.append(item)
    top=len(stk)-1

def Pop_(stk):
    if isEmpty(stk):
        return "Underflow"
    else:
        item = stk.pop()
        if isEmpty(stk):
            top=None
        else:
            top=len(stk)-1

        return item

def Peek(stk):
    if isEmpty(stk):
        return "Underflow"
    top=len(stk)-1
    return stk[top]

def Display(stk):
    if isEmpty(stk):
        print("Stack underflow")
    
    top=len(stk)-1
    n=len(stk)

    print(stk[top],"<----- top") 
    for i in range(top-1,-1,-1):
        print(stk[i])


while True:
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice=int(input("Enter your choice: "))
    if choice==1:
        item=int(input("Enter the number: "))
        Push(item,lst)

    elif choice==2:
        item=Pop_(lst)
        if item!="Underflow":
            print(item)

    elif choice==3:
        item=Peek(lst)
        print(item)

    elif choice==4:
        Display(lst)
    
    elif choice==5:
        break
    
    else:
        print("Please make a valid choice.")