n = int(input())
nums = input().split()
A = []
for i in nums:
    A.append(int(i))
A.sort()
m = int(input())
finds = input().split()
arr = []
for i in finds:
    arr.append(int(i))

for num in arr:
    lt, rt = 0, n - 1
    result = 0
    
    while lt <= rt:
        mid = (lt + rt) // 2
        if (num == A[mid]):
            result = 1
            break
        elif num > A[mid]:
            lt = mid + 1
        else :
            rt = mid - 1
    
    print(result)