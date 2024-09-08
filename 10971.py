n = int(input())

arr = []
flags = [False] * n
min = float("inf")

for i in range(n):
    temp = input().split()
    temp = [int(x) for x in temp]
    arr.append(temp)
        
def DFS(start, current, arr, cost, flags):
    global min
    
    if (not False in flags):
        if (arr[current][start] != 0):
            cost += arr[current][start]
            if (cost < min):
                min = cost
    
    else :
        for i in range(n):
            if (flags[i] == False and arr[current][i] != 0 and cost + arr[current][i] < min):
                flags[i] = True
                DFS(start, i, arr, cost + arr[current][i] , flags)
                flags[i] = False
            
for t in range(n):
    flags[t] = True
    DFS(t, t, arr, 0, flags)
    flags[t] = False
    
print(min)