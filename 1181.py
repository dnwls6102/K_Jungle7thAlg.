import sys

n = int(sys.stdin.readline())
array = []

for i in range(n):
    array.append(sys.stdin.readline().strip())

array = list(set(array))
array.sort()
array.sort(key = len)

for i in array:
    print(i)
