from collections import deque
import sys

n = int(input())

queue = deque()

for i in range(n):
    command = sys.stdin.readline().strip().split()
    if (command[0] == "push"):
        queue.appendleft(int(command[1]))
    elif (command[0] == "pop"):
        if (len(queue) == 0):
            print(-1)
        else:
            print(queue.pop())
    elif (command[0] == "size"):
        print(len(queue))
    elif (command[0] == "empty"):
        if (len(queue) == 0):
            print(1)
        else:
            print(0)
    elif (command[0] == "front"):
        if (len(queue) == 0):
            print(-1)
            continue
        temp = queue.pop()
        print(temp)
        queue.append(temp)
    elif (command[0] == "back"):
        if (len(queue) == 0):
            print(-1)
            continue
        temp = queue.popleft()
        print(temp)
        queue.appendleft(temp)