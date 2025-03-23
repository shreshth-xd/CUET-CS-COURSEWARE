# Using Stacks to evaluate a postfix expression:

stack=[]

inputExpr = str(input("Enter the postfix expression: "))
while ("(" or ")") in inputExpr:
    inputExpr = str(input("Enter the postfix expression again: "))

operators={"+":0,"-":1,"*":2,"/":3,"%":4}

def Push(item,stk):
    if item.isnum():
        stk.push(item)
    elif item in "+-*/%":
        b,a = stk.pop(),stk.pop()
        result=[a+b,a-b,a*b,a/b,a%b][operators[item]]
        stack.append(result)

print("The value of your given postfix expression is:",stack[0])