import sys

class stack():
    def __init__(self):
        self.arr = []
    def is_empty(self):
        if len(self.arr) == 0:
            print(1)
        else:
            print(0)
    def push(self, num):
        self.arr.append(num)
    def pop(self):
        if (len(self.arr) == 0):
            print(-1)
        else:
            temp = self.arr[-1]
            self.arr = self.arr[:-1]
            print(temp)
    def size(self):
        print(len(self.arr))
    def top(self):
        if (len(self.arr) == 0):
            print(-1)
        else:
            print(self.arr[-1])

n = int(input())
st = stack()
for i in range(n):
    command = sys.stdin.readline().split()
    if (command[0] == "push"):
        st.push(int(command[1]))
    elif (command[0] == "pop"):
        st.pop()
    elif (command[0] == "size"):
        st.size()
    elif (command[0] == "empty"):
        st.is_empty()
    elif (command[0] == "top"):
        st.top()    