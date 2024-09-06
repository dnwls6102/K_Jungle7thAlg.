def hanoi(n, from_, via_, to_): 
    if (n == 1):
        print(from_, to_)
        
    else:
        hanoi(n-1, from_, to_, via_) #가장 밑에 깔린 n번째 원반을 목적지로 이동시키기 위해 n-1개의 원반들을 빈 자리로 이동시킴
        print(from_, to_) #from_줄의 n번째 원반(가장 아래 깔린 원반)이 이동함
        hanoi(n-1, via_, from_, to_) #from_으로 이동하기 위해 잠시 via_에 들른 n-1개의 원반들이 목적지로 이동함

n = int(input())
print((2**n - 1))
if (n <= 20):
    hanoi(n, 1, 2, 3)
