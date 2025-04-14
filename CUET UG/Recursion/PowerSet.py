string=str(input("Enter the string: "))

def PowerSetGenerator(string,ptr=0,current="",combs=None):
    if ptr==len(string):
        return combs

    elif combs is None:
        combs = set()
        combs.add(current)
        return PowerSetGenerator(string,ptr+1,current+string[ptr],combs=combs)

    elif current in combs:
        return PowerSetGenerator(string,ptr+1,current+string[ptr],combs=combs)
        
    elif current not in combs:
        combs.add(current)
        return PowerSetGenerator(string,ptr+1,current,combs=combs)
    
    
print(PowerSetGenerator(string))