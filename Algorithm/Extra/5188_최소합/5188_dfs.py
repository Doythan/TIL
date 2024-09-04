def min_path_sum_dfs(grid):
    N = len(grid)
    memo = [[-1] * N for _ in range(N)]

    def dfs(x, y):
        # 목적지에 도착하면 현재 셀의 값을 반환
        if x == N - 1 and y == N - 1:
            return grid[x][y]

        # 메모이제이션: 이미 계산한 경우 반환
        if memo[x][y] != -1:
            return memo[x][y]

        # 이동할 수 있는 방향 (오른쪽, 아래쪽)
        directions = [(0, 1), (1, 0)]
        min_sum = float('inf')

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                # DFS로 다음 셀을 탐색하고 최소 합을 계산
                min_sum = min(min_sum, dfs(nx, ny))

        # 현재 셀의 값에 다음 셀로부터의 최소 합을 더하여 메모이제이션
        memo[x][y] = grid[x][y] + min_sum
        return memo[x][y]

    # DFS 시작
    return dfs(0, 0)


# 입력 처리
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    result = min_path_sum_dfs(grid)
    print(result)
