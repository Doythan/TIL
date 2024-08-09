N = int(input())
arr1 = [list(map(int, input().split())) for _ in range(N)]
arr2 = [list(map(int, input())) for _ in range(N)]
print(arr1)
print(arr2)

arr1 = [0] * N
arr2 = [[0] * N for _ in range(N)]
print(arr1)
print(*arr1)
print(arr2)

for i in range(N):
    print(*arr2[i])

for i in range(N):
    for j in range(N):
        print(arr2[i][j], end=' ')
    print(arr2)

# *********개꿀팁***********
N = int(input())

# 2차원 배열 주변 0으로 1바퀴 감싸며 입력 (for)
matrix = [[0] * (N+2)]
for _ in range(N):
    matrix += [[0] + list(map(int, input().split())) + [0]]
matrix += [[0] * (N+2)]

# 2차원 배열 주변 0으로 감싸며 입력 (리컴)
matrix = [[[0] * (N+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N+2)]]

print(matrix)

