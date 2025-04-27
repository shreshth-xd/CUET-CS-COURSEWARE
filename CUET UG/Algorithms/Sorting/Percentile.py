# To calculate the xth percentile where x is a number between 0 and 100

def bubbleSort(array,length):
    for i in range(0,length):
        for j in range(0,n-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]

    return array

marks=[]
n=int(input("Enter how many marks do you want to enter: "))
for i in range(n):
    individualX=int(input("Enter the score: "))
    marks.append(individualX)

sortedMarks=bubbleSort(marks)
x=int(input("Enter the x(between 0 to 100): "))
percentile=int(round((x*n)/100,0))
print(f"{x}th percentile is {percentile}")