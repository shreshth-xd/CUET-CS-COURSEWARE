# Implementing chaining method for collision resolution in Hash maps/Hash tables in Python

class HashTable:
    def __init__(self,size=100):
        self.MAX=size
        self.arr = [[] for i in range(self.MAX)]
    
    def GetHash(self,key):
        HashValue=0
        for i in key:
            HashValue+=ord(i)
        return HashValue
    
    def add(self,key,value):
        h=self.GetHash(key)
        found=False
        for idx,element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[h][idx] = (key,value)
                found=True
                break

        if not found:
            self.arr[h].append((key,value))

    def get(self,key):
        h=self.GetHash(key)
        for idx,element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                return element[1]
    
    # To delete a key value pair from the Hash table
    def delItem(self,key):
        hash=self.GetHash(key)
        for index,element in enumerate(self.arr[hash]):
            if len(element)==2 and element[0]==key:
                del self.arr[hash][index]