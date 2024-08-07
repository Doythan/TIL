import sys
sys.stdin = open("input.txt", "r")


# def find_way(node):
#     if node == 99:  # 도착지에 도달했는지 확인
#         return 1
#     visited[node] = True  # 현재 노드를 방문 처리
#     for next_node in graph[node]:
#         if not visited[next_node]:
#             if find_way(next_node):  # 재귀적으로 경로를 탐색
#                 return 1
#     return 0
#
#
# for _ in range(10):
#     tc, n = map(int, input().split())  # 테스트 케이스 번호와 순서쌍 수
#     a = list(map(int, input().split()))
#
#     # 그래프 초기화
#     graph = [[] for _ in range(100)]
#     for i in range(0, len(a), 2):
#         graph[a[i]].append(a[i + 1])
#
#     # 방문 처리 배열 초기화
#     visited = [False] * 100
#
#     # 출발점은 0번 노드
#     result = find_way(0)
#     print(f'#{tc} {result}')
'''
1 16
0 1 0 2 1 4 1 3 4 8 4 3 2 9 2 5 5 6 5 7 7 99 7 9 9 8 9 10 6 10 3 7
[[1, 2], [4, 3], [9, 5], [7], [8, 3], [6, 7], [10], [99, 9], [], [8, 10]
'''


def DFS_f(v):
    if v == 99:
        return 1
    visited[v] = 1
    for next_v in graph[v]:
        if visited[next_v] == 0:
            if DFS_f(next_v):
                return 1
    return 0


for tc in range(10):                          # 테스트 케이스 10개 반복
    tc, e = map(int, input().split())         # 테스트 케이스 번호, 간선 총 갯수
    edges = list(map(int, input().split()))   # 순서쌍 입력
    graph = [[] for _ in range(101)]          # 그래프 초기화, 예) 0번 정점에서 갈 수 있는 정점을 graph[0][*] *에 넣는다.
    visited = [0] * 100                       #
    for i in range(e):
        v1, v2 = edges[i*2], edges[i*2+1]
        graph[v1].append(v2)
    print(f'#{tc}', DFS_f(0))






