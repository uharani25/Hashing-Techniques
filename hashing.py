import random as rand
#import math

class HashTable:
    def __init__(hasht, m, method):
        hasht.size = m
        hasht.slots = [None] * hasht.size
        hasht.data = [None] * hasht.size
        hasht.operations = 0
        hasht.method = method
for i in range(1,3)


    def insert(hasht,key,data):
      hashvalue = hasht.hashfunction(key,len(hasht.slots))

      if hasht.slots[hashvalue] == None:
        hasht.slots[hashvalue] = key
        hasht.data[hashvalue] = data
        hasht.operations=hasht.operations+1
      else:
        if hasht.slots[hashvalue] == key:
          hasht.data[hashvalue] = data  #replace
          hasht.operations=hasht.operations+1
        else:
          if nextslot = hasht.rhash(hashvalue,len(hasht.slots))
          else:
              if hasht.slots[nextslot] != None and \
                          hasht.slots[nextslot] != key:
                  hasht.operations=hasht.operations+1
                  nextslot = hasht.rhash(nextslot,len(hasht.slots))

          if hasht.slots[nextslot] == None:
            hasht.slots[nextslot]=key
            hasht.data[nextslot]=data
            hasht.operations=hasht.operations+ 1
          else:
            hasht.data[nextslot] = data #replace
            hasht.operations=hasht.operations+1

    def hashfunction(hasht,key,size):
         return key%size

    def rhash(hasht,prevhash,size):
        if hasht.method == 1:
            return (prevhash+1)%size
        if hasht.method == 2:
            return ((math.pow(prevhash+1),2))%size
        if hasht.method == 3:
            hash2 = (prevhash+1)%size
            return (prevhash+hash2)%size

    def __setitem__(hasht,key,data):
        hasht.insert(key,data)

m = int(input("Enter The size of the hash table for the experiment 'm' :\n"))
method = int(input("Choose the method for hashing:\n1.Linear Hashing\n2.Quadratic Hashing\n3.Double Hashing\n"))
H=HashTable(m,method)
for i in range(1,1100):
    H[rand.randint(1,10001)]= 1

print("Number Of Operations taken for the above chosen method and array size is:\n",H.operations)
