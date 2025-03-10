"""
A happy number is a number whose eventual sum of the sqaure of the digits equals to 1.

Non happy repeats themselves or repeats a number which has been a part of this repetitive addition process.
"""

def sum_sq_digits(n,sum=0):
    if n>0:
        rem=n%10
        sum+=rem**2
        sum_sq_digits(n//10,sum)
    else:
        return sum
    
def IsHappy(n,visited=None):
    if n==1:
        return True
    if n==0:
        return False
    else:
        if visited is None:
            visited = set()
        
        if n in visited:
            """
            Now right exactly here we are detecting non happy numbers, which repeat themselves
            """
            return False
        
        visited.add(n)
        nextNumber=sum_sq_digits(n)
        return IsHappy(nextNumber,visited)

n=int(input("Enter the number to check if the number is a happy number or not: "))
result = IsHappy(n)
print(result)