# Presenting the most basic usage of try-except blocks out there
# As we all know that it's illegal to divide a number by 0, both in Computer science and Mathematics

try:
    num=int(input("Enter a number: "))
    print(num/0)
except ZeroDivisionError:
    print("Division by 0 is not permissable.")