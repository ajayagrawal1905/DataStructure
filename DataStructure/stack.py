'''
Author Name : Ajay Manoj Agrawal
Github Link : https://github.com/ajayagrawal1905
Date : 05-01-2021 Tuesday

'''
from collections import deque

class Stack:
    
    def __init__(self):
        self.container = deque()

    def push(self,val):
        self.container.append(val)
    
    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

st = Stack()
st.push("ajay")
st.push("sanket")
st.push("rohit")
print(st.peek())
print(st.pop())
print(st.pop())
print(st.pop())
print(st.is_empty())