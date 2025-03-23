"""
Algorithm for infix to postfix conversion:

1. If a left bracket is encountered, push it to the stack.
2. If an operator is encountered, push it to the stack.
3. If an operand is encountered, add it to the string
4. If a right bracket is encountered, pop the elements from the stack until the left bracket is popped,
and add all these popped elements (except the right bracket) to the expression

"""

stack=[]
expression=""
chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
numbers="0123456789"
operators="+-*/%"
top=None

def Push(item,stk):
    if item=="(":
        stk.append(item)
    elif item in operators:
        stk.append(item)
    top=len(stk)-1

def Pop_(item,stk):
    while item!="(":
        item=stk.pop()
        if item!=")" and item!="(":
            expression+=item

infixExpr = str(input("Enter the expression: "))
for i in range(0, len(infixExpr)):
    if infixExpr[i] in (chars or numbers):
        expression+=infixExpr[i]
    elif (infixExpr[i]=="(") or (infixExpr[i] in operators):
        Push(infixExpr[i],stack)
    elif infixExpr[i]==")":
        Pop_(infixExpr[i],stack)

print("Infix expression:",infixExpr)
print("Postfix expression:",expression)