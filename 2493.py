import copy

class stack():
    def __init__(self):
        self.arr = []
    def is_empty(self):
        if len(self.arr) == 0:
            return 1
        else:
            return 0
    def push(self, num):
        self.arr.append(num)
    def pop(self):
        if (len(self.arr) == 0):
            return -1
        else:
            temp = self.arr[-1]
            self.arr = self.arr[:-1]
            return temp
    def size(self):
        return len(self.arr)
    def top(self):
        if (len(self.arr) == 0):
            return -1
        else:
            return self.arr[-1]

n = int(input())
st = stack()
result = []
tops = input().split()
tops = [int(x) for x in tops]
for t in tops:
    st.push(t)

while (not st.is_empty()):
    target = st.pop()
    temp = copy.deepcopy(st)
    while (True):
        if target < temp.top():
            result.append(temp.size())
            break
        else:
            temp.pop()
            if (temp.is_empty()):
                result.append(temp.size())
                break

for i in range(n-1, -1, -1):
    print(result[i], end=" ")