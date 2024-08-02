import sys
sys.stdin = open('input.txt', 'r')

dxy = [[1, 0], [0, -1], [0, 1]]


def search_leader(x, y):
    visited = [[0] * BLOCK_SIZE for _ in range(BLOCK_SIZE)]
    visited[x][y] = 1  # 시작지점을 방문체크 함
    while x != BLOCK_SIZE - 1:
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= BLOCK_SIZE or ny < 0 or ny >= BLOCK_SIZE:
                continue
            if not data[nx][ny]:
                continue
            if visited[nx][ny]:
                continue
            visited[x][y] = 1
            x, y = nx, ny
    if data[x][y] == 2:
        return True
    return False


for _ in range(1, 11):
    tc = int(input())
    BLOCK_SIZE = 100
    data = [list(map(int, input().split())) for _ in range(BLOCK_SIZE)]
    result = -1
    for j in range(BLOCK_SIZE):
        if data[0][j] == 0:
            continue
        if search_leader(0, j):
            result = j
            break
    print(f"#{tc} {result}")
