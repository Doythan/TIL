import sys
sys.stdin = open("input.txt", "r")


def DFS(vv):
    if vv == e_v:  # 현재 노드가 목표 노드인 경우
        return 1  # 경로를 찾았음을 표시
    visited[vv] = 1  # 현재 노드를 방문했다고 표시
    for next_vv in graph[vv]:  # 현재 노드와 연결된 모든 노드에 대해
        if visited[next_vv] == 0:  # 다음 노드가 방문되지 않은 경우
            if DFS(next_vv):  # 다음 노드를 탐색
                return 1  # 경로를 찾았으면 1 반환
    return 0  # 모든 경로를 탐색했지만 찾지 못한 경우 0 반환


# 테스트 케이스 수 입력
T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())  # 정점과 간선의 수 입력
    graph = [[] for _ in range(V + 1)]  # 그래프 초기화 (정점 번호는 1부터 시작)
    visited = [0] * (V + 1)  # 방문 리스트 초기화 (정점 번호는 1부터 시작)

    # 간선 정보 입력
    for _ in range(E):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)  # v1에서 v2로 가는 간선을 그래프에 추가

    # 시작 노드와 목표 노드 입력
    s_v, e_v = map(int, input().split())

    # DFS 탐색 결과 출력
    print(f'#{tc}', DFS(s_v))

# def DFS(vv):
#     if vv == e_v:
#         return 1
#     visited[vv] = 1
#     for next_vv in graph[vv]:
#         if visited[next_vv] == 0:
#             if DFS(next_vv):
#                 return 1
#     return 0
#
#
# T = int(input())
# for tc in range(1, T+1):
#     V, E = map(int, input().split())
#     graph = [[] for _ in range(V+1)]
#     visited = [0] * (V+1)
#     for _ in range(E):
#         v1, v2 = map(int, input().split())
#         graph[v1].append(v2)
#     s_v, e_v = map(int, input().split())
#     print(f'#{tc}', DFS(s_v))

