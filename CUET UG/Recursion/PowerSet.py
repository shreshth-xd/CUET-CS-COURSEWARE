string=str(input("Enter the string: "))

def PowerSetGenerator(string,ptr=0,current="",combs=None):
    if combs is None:
        combs = set()
    
    if ptr==len(string):
        combs.add(current)
        return combs
    

    # To include a combination
    PowerSetGenerator(string, ptr+1, current+string[ptr], combs)
    
    # To exclude a combination
    PowerSetGenerator(string, ptr+1, current, combs)

    return combs
    
print(PowerSetGenerator(string))