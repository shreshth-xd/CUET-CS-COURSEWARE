# To find the sum of the digits of the number until it reduces to a single digit

def SumOfDigits(num,sum=0):
    if sum//10==0:
        return sum
    rem=num%10
    sum+=rem
    return SumOfDigits(num//10,sum)

n=int(input("Enter the number: "))
res=SumOfDigits(n)
print(res)