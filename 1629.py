cmd = [int (x) for x in input().split()]
a, b, c = cmd[0], cmd[1], cmd[2]

def mul(a, b, c):
    if b == 1:
        return a % c
    else:
        tmp = mul(a, b//2, c)
        if (b % 2) == 0:
            return (tmp * tmp) % c
        else:
            return (tmp * tmp * a) % c

print(mul(a,b,c))