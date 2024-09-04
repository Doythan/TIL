from collections import deque


def BFS(x, y):
    queue = deque()



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    dx = [0, 0, -1, 1]
    dy = []
    BFS(0, 0)

