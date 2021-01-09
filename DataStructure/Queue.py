'''
Author Name : Ajay Manoj Agrawal
Github Link : https://github.com/ajayagrawal1905/DataStructure/
Date : 06-01-2021 Wed

'''
from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self,val):
        self.buffer.appendleft(val)
    
    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)

    
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.dequeue())
print(q.is_empty())
print(q.size())
