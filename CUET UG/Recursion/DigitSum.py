# To find the sum of the digits of the number until it reduces to a single digit

def SumOfDigits(num,sum=0):
    if num//10==0:
        return num
    rem=num%10
    sum+=rem
    return SumOfDigits(num//10,sum)