def is_prime_number(n):
    if n < 2:
        return False
    for i in range(2, n):
        if (n % i == 0):
            return False
    return True

n = int(input())
nums = input().split()
temp = 0
for i in nums:
    if is_prime_number(int(i)):
        temp += 1
print(temp)
