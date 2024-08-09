# DP (동적계획) 활용 피보난치 수열, 모든 문제를 DP로 풀 수는 없다 시간이 더 걸리는 경우도 있다.
def fibo_n(n):
    f = [0] * (n+1)
    f[0], f[1] = 0, 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]


result = fibo_n(8)
print(result)