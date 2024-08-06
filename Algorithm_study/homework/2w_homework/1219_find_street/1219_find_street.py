# import sys
# sys.stdin = open("input.txt", "r")
#
# def find_way():
#     temp = 99
#     for i in range(len(a)):
#         if i % 2 == 1 and a[i] == temp:
#             if a[i-1] == 0:
#                 return 1
#             elif a[i-1] != 0:
#                 temp = a[i-1]
#                 return find_way()
#     return False
#
#
# for _ in range(10):
#     tc, n = map(int, input().split())  # 테스트 케이스 번호와 순서쌍 수
#     a = list(map(int, input().split()))
#     result = find_way()
#     print(f'#{1} {result}')

import sys
sys.stdin = open("input.txt", "r")


# def find_way(temp):
#     for i in range(len(a)):
#         if i % 2 == 1 and a[i] == temp:
#             if a[i-1] == 0:
#                 return 1
#             elif a[i-1] == temp:
#                 a[i-1], a[i] = 100, 100
#                 return find_way(temp)
#             else:
#                 return find_way(a[i-1])
#         elif i == (len(a) - 1) and a[i] != temp:
#             temp = 99
#
#     return 0
#
#
# # for _ in range(10):
# tc, n = map(int, input().split())  # 테스트 케이스 번호와 순서쌍 수
# a = list(map(int, input().split()))
# k = len(a)
# result = find_way(99)
# print(f'#{tc} {result}')

import sys

sys.stdin = open("input.txt", "r")


def find_way(node):
    if node == 99:  # 도착지에 도달했는지 확인
        return 1
    visited[node] = True  # 현재 노드를 방문 처리
    for next_node in graph[node]:
        if not visited[next_node]:
            if find_way(next_node):  # 재귀적으로 경로를 탐색
                return 1
    return 0


for _ in range(10):
    tc, n = map(int, input().split())  # 테스트 케이스 번호와 순서쌍 수
    a = list(map(int, input().split()))

    # 그래프 초기화
    graph = [[] for _ in range(100)]
    for i in range(0, len(a), 2):
        graph[a[i]].append(a[i + 1])

    # 방문 처리 배열 초기화
    visited = [False] * 100

    # 출발점은 0번 노드
    result = find_way(0)
    print(f'#{tc} {result}')



