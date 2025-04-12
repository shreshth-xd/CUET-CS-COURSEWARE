string=str(input("Enter the string: "))

def PowerSetGenerator(string,ptr=0,combs=None):
    if combs is None:
        combs = set()

    if ptr in combs:
        return PowerSetGenerator(string[ptr+1:],combs=combs)
        pass
    
    combs.add("")
    combs.add(string[ptr])    
