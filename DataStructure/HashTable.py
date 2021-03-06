'''
Author Name : Ajay Manoj Agrawal
Github Link : https://github.com/ajayagrawal1905/DataStructure/
Date : 31-12-2020 Thu

'''
class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None

t = HashTable()
t['ajay'] = 1905
t['rohit'] = 1507
t['sanket'] = 1010
print(t['rohit'])
print(t['ajay'])
del t['ajay']
print('ajay :',t['ajay'])