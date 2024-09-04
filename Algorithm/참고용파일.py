from collections import deque


def bfs(maze, start, end):
    n = len(maze)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우
    queue = deque([(*start, 0)])  # (x, y, 거리)
    visited = set()
    visited.add(start)

    while queue:
        x, y, dist = queue.popleft()

        if (x, y) == end:
            return dist

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited and maze[nx][ny] == 0:
                visited.add((nx, ny))
                queue.append((nx, ny, dist + 1))

    return 0


def solve_maze(maze):
    n = len(maze)
    start = (0, 0)
    end = (n - 1, n - 1)
    return bfs(maze, start, end)


# 예시 입력 처리
t = int(input())  # 테스트 케이스 수
for _ in range(t):
    n = int(input())  # 미로의 크기
    maze = [list(map(int, input().split())) for _ in range(n)]
    result = solve_maze(maze)
    print(result)
