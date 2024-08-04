n = int(input())
a = list(map(int, input().split()))
counts = [0] * (5+1)
temp = [0] * n
for i in range(n):
    counts[a[i]] += 1
for i in range(1, 5+1):
    counts[i] += counts[i-1]
for i in range(n-1, -1, -1):
    counts[a[i]] -= 1
    temp[counts[a[i]]] = a[i]
print(temp)