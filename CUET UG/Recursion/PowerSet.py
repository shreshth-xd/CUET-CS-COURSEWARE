string=str(input("Enter the string: "))

def PowerSetGenerator(string,ptr=0,combs=None):
    if combs is None:
        combs = set()
        combs.add("")


    if string in combs:
        return PowerSetGenerator(string[0]+string[ptr+1:],combs=combs)
        pass
    
    if string not in combs:
        combs.add(string)
        return PowerSetGenerator(string)