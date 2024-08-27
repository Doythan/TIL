# Memoization을 활용한 fibo

def fibo_n(n):
    global momo
    if n >= 2 and memo[n] == 0:
        memo[n] = fibo_n(n-1) + fibo_n(n-2)
    return memo[n]


n = 10
memo = [0] * (n+1)
momo[0], memo[1] = 0, 1
result = fibo_n(n)
print(result)
