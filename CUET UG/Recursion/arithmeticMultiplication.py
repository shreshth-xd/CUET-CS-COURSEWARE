# Using recursion to compute the product of two numbers without using the multiplication operator

def product(x,y):
    if y==1:
        return x
    else:
        return x+product(x,y-1)

a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
res=product(a,b)
print(a,"X",b,"=",res)