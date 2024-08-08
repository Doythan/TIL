
# 백트래킹 미로문제 예시 )
def is_safe(maze, x, y, solution):
    """
    미로에서 (x, y) 위치가 안전한지 확인
    """
    n = len(maze)
    return 0 <= x < n and 0 <= y < n and maze[x][y] == 0 and solution[x][y] == 0


def solve_maze_util(maze, x, y, solution):
    """
    (x, y) 위치에서 미로를 해결하는 유틸리티 함수
    """
    n = len(maze)
    # 목적지에 도달했는지 확인
    if x == n - 1 and y == n - 1 and maze[x][y] == 0:
        solution[x][y] = 1
        return True

    if is_safe(maze, x, y, solution):
        # 현재 위치를 해결 경로에 포함
        solution[x][y] = 1

        # 아래로 이동
        if solve_maze_util(maze, x + 1, y, solution):
            return True

        # 오른쪽으로 이동
        if solve_maze_util(maze, x, y + 1, solution):
            return True

        # 만약 이동이 실패하면 해결 경로에서 제외 (백트래킹)
        solution[x][y] = 0

    return False


def solve_maze(maze):
    """
    미로 문제를 해결하는 함수
    """
    n = len(maze)
    solution = [[0 for _ in range(n)] for _ in range(n)]

    if not solve_maze_util(maze, 0, 0, solution):
        print("Solution doesn't exist")
        return None

    return solution


# 예제 미로
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

solution = solve_maze(maze)

if solution:
    for row in solution:
        print(row)
else:
    print("No solution found")
