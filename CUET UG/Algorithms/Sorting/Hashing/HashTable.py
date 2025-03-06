# Implementing Hashing in Python using lists and classes

class HashMap:
    def __init__(self,size=100):
        self.MAX = size
        self.arr = [None for i in range(self.MAX)]
    
    def getHash(self,key):
        sum=0
        for i in key:
            sum+=ord(i)
        
        hash=sum%10
        return hash

    def add(self,key,value):
        index=self.getHash(key)
        self.arr[index] = value
    
    def get(self,key):
        index=self.getHash(key)
        return self.arr[index]
    

HashTable = HashMap()
key=input("Enter the key: ")
value=input("Enter it's corresponding value: ")
HashTable.add(key,value)
print(HashTable.get(key))