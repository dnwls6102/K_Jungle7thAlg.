import heapq
import sys

n = int(input())

arr = []

for i in range(n):
    cmd = int(sys.stdin.readline())
    if (cmd == 0):
        if (len(arr) == 0):
            print(0)
        else:
            tmp = heapq.heappop(arr)
            print(-tmp)
    else:
        heapq.heappush(arr, -cmd)

