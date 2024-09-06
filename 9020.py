import sys

def is_prime_number(n):
    if n < 2:
        return False
    for i in range(2, n):
        if (n % i == 0):
            return False
    return True

n = int(sys.stdin.readline())

for i in range(n):
    temp = []
    x = int(sys.stdin.readline())
    for t in range(int(x/2), 1, -1):
        if is_prime_number(t) and is_prime_number(x-t):
                is_min = x-t-t
                temp = [t, (x-t)]
                break
        
    print(temp[0], temp[1])
            
            


