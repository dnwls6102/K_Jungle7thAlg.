import sys
sys.setrecursionlimit(10**8)

n = int(sys.stdin.readline())
arr = []

for x in range(n):
    temp = sys.stdin.readline().rstrip()
    arr.append(list(temp))
    
result = ""

def eisou(arr, n, index):
    global result
    pixel = arr[index[0]][index[1]]
    for y in range(index[0], index[0] + n):
        for x in range(index[1], index[1] + n):
            if (pixel != arr[y][x]):
                result += "("
                eisou(arr, n//2, index)
                eisou(arr, n//2, (index[0], index[1] + n//2))
                eisou(arr, n//2, (index[0]+ n//2, index[1]))
                eisou(arr, n//2, (index[0] + n//2, index[1] + n//2))
                result += ")"
                return
    result += str(pixel)
    
eisou(arr, n, (0,0))
print(result)
    