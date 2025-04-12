string=str(input("Enter the string: "))

def PowerSetGenerator(string,ptr,combs=None):
    if combs is None:
        combs = set()

    if ptr in combs:
        pass
    
    combs.add("")
    combs.add(ptr)    
    