string=str(input("Enter the string: "))

def PowerSetGenerator(string,ptr=-1,current="",combs=None):
    if combs is None:
        combs = set()
        combs.add("")
        return PowerSetGenerator(string,combs=combs)

    elif current in combs:
        PowerSetGenerator(string,ptr+1,current+string[ptr],combs=combs)
        pass
    
    elif current not in combs:
        combs.add(current)
        PowerSetGenerator(string,ptr+1,current,combs=combs)
    
    elif ptr==len(string):
        return combs