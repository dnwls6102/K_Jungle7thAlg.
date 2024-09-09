import sys

n = int(input())
st = []
result = []
tops = sys.stdin.readline().split()
tops = [0] + [int(x) for x in tops]

for i in range(1, n + 1):
    while (not len(st) == 0) :
        if (tops[st[-1]] > tops[i]):
            result.append(st[-1])
            break
        else:
            st.pop()
    if (len(st) == 0):
        result.append(0)
    st.append(i)
        
for x in result:
    print(x, end=" ")