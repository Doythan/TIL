N = int(input())

# 2차원 배열 주변 0으로 감싸며 입력 (for)
# matrix = [[0] * (N+2)]
matrix = []
for _ in range(N):
    matrix += [list(map(int, input().split()))]
# matrix += [[0] * (N+2)]

# 2차원 배열 주변 0으로 감싸며 입력 (리컴)
# matrix = [[[0] * (N+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N+2)]]
#
print(matrix)

