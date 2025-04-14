string=str(input("Enter the string: "))

def PowerSetGenerator(string,ptr=-1,current="",combs=None):
    if combs is None:
        combs = set()
        combs.add("")
        return PowerSetGenerator(string[ptr+1],combs=combs)

    elif string in combs:
        return PowerSetGenerator(string[0]+string[ptr+1:],combs=combs)
        pass
    
    elif string not in combs:
        combs.add(string)
        return PowerSetGenerator(string[ptr+1],combs=combs)
    
    elif ptr==len(string):
        return combs