from collections import deque

command = input().split()
n = int(command[0])
k = int(command[1])
queue = deque()
result = []


for i in range(1, n+1):
    queue.appendleft(i)

count = 0

while (len(result) < n):
    count += 1
    if (count != k):
        temp = queue.pop()
        queue.appendleft(temp)
    else :
        result.append(queue.pop())
        count = 0

print("<", end="")
for i in result[0 : n-1]:
    print(i, end = ", ")
print(result[-1], end="")
print(">")