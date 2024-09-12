import heapq


def dijkstra_min_distance(V, edges):
    # 그래프 초기화
    graph = [[] for _ in range(V + 1)]
    for u, v, w in edges:
        graph[u].append((v, w))
    print(graph)

    # 최소 거리 배열 초기화
    dist = [float('inf')] * (V + 1)
    dist[0] = 0  # 시작점은 0으로 초기화

    # 우선순위 큐 초기화 (비용, 노드)
    pq = [(0, 0)]  # (비용, 시작점)

    while pq:
        current_dist, u = heapq.heappop(pq)

        # 이미 처리된 경우 무시
        if current_dist > dist[u]:
            continue

        # 현재 노드 u에서 연결된 모든 노드 v 탐색
        for v, w in graph[u]:
            # v로 이동하는 비용을 계산하고, 기존 값보다 작으면 갱신
            next_dist = current_dist + w
            if next_dist < dist[v]:
                dist[v] = next_dist
                heapq.heappush(pq, (next_dist, v))

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

print(dijkstra_min_distance(V, edges))
