import sys
sys.setrecursionlimit(10**8)

n = int(input())
col = [0] * (n + 1)
visited = [False] * (n + 1)
result = 0

#i(col의 index값) = 체스말의 x 값
#예: col[1] = 3 => 좌상단이 (0,0)이라고 했을 때, (1,3)번째 위치
def nQueen(i, col):
    global result
    n = len(col) - 1
    
    #만약 기준 체스말의 같은 행, 혹은 대각선에 또다른 체스말이 없다면
    if (promising(i, col)) :
        if (i == n) : # 마지막 째 체스말(n번째 행)까지 검사가 완료된거면
           # print(col[1 : n + 1]) 
           result += 1 # type: ignore
           return
            


        else : #아직 마지막 째 체스말까지 검사가 되지 않았다면
            for j in range(1, n+1):
                col[i + 1] = j # 다음 깊이의 1, 2, 3 ... n번째 칸까지 검사시키기
                #재귀호출
                nQueen(i+1, col) # type: ignore

    
    
def promising(i, col):
    flag = True
    k = 1
    
    #i 직전의 깊이까지 검사 (i직전까지의 값은 nQueen의 else 부분에서 검사했으니)
    while(k < i and flag):
        #같은 열에 체스말이 있거나, 대각선 위치에 체스말이 있는 경우
        if(col[i] == col[k] or abs(col[i] - col[k]) == (i-k)):
            flag = False
        k += 1
    return flag

nQueen(0, col)
print(result)