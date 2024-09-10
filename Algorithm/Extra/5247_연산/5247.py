import sys
sys.stdin = open("input.txt", "r")

from collections import deque


def bfs(N):
    visited = [False] * 1000001
    queue = deque([(N, 0)])
    visited[N] = True
    while queue:
        now, cnt = queue.popleft()

        if now == M:
            return cnt

        for next in (now + 1, now - 1, now * 2, now - 10):
            if 0 <= next < 1000001 and not visited[next]:
                visited[next] = True
                queue.append((next, cnt + 1))


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    result = bfs(N)
    print(f'#{tc}', result)



