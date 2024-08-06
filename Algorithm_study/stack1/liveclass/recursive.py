재귀호출

# 팩토리얼
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)


print(factorial(5))

# 피보나치
def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)


n = 6
result = fibo(n)
print(result)

# 모든 배열 원소에 접근하기
def f(i, N):  # i는 현재 인덱스, N 크기
    if i == N:
        return
    print(arr[i])
    f(i+1, N)
    return


arr = [1, 2, 3]
N = len(arr)
f(0, N)

배열에 v가 있으면 1, 없으면 0을 리턴
















