from collections import deque


def bfs_min_distance(V, edges):
    # 그래프 초기화
    graph = [[] for _ in range(V + 1)]
    for u, v, w in edges:
        graph[u].append((v, w))

    # 최소 거리 배열 초기화
    dist = [float('inf')] * (V + 1)
    dist[0] = 0  # 시작점은 0으로 초기화

    # BFS에 사용할 큐
    queue = deque([0])

    while queue:
        u = queue.popleft()

        # 현재 노드 u에서 연결된 모든 노드 v 탐색
        for v, w in graph[u]:
            # v로 이동하는 비용을 계산하고, 기존 값보다 작으면 갱신
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                queue.append(v)

    return dist[V]  # 목표지점 V까지의 최소 거리 반환


# 예시 입력
V = 3  # 노드 개수
edges = [
    (0, 1, 1),
    (0, 2, 3),
    (1, 2, 1),
    (1, 3, 6),
    (2, 3, 2)
]

print(bfs_min_distance(V, edges))
