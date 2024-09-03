import sys
from collections import deque


def solution():
    input = sys.stdin.read
    data = input().splitlines()

    n = int(data[0])  # 노드의 개수
    graph = [[] for _ in range(n + 1)]

    # 그래프를 인접 리스트로 표현
    for i in range(1, n):
        a, b = map(int, data[i].split())
        graph[a].append(b)
        graph[b].append(a)

    # 부모 노드를 저장할 리스트
    parent = [0] * (n + 1)

    # BFS를 이용한 탐색
    queue = deque([1])  # 1번 노드를 루트로 시작
    parent[1] = -1  # 루트의 부모는 없으므로 -1로 표시

    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            if parent[neighbor] == 0:  # 아직 부모가 정해지지 않은 경우
                parent[neighbor] = node
                queue.append(neighbor)

    # 2번 노드부터 부모를 출력
    for i in range(2, n + 1):
        print(parent[i])


# 예제 실행
solution()
