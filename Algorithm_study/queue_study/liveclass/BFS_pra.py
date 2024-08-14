# import sys
# sys.stdin = open("input.txt", "r")

V, E = map(int, input().split())  # V : 노드 개수 E : 간선 개수
arr = list(map(int, input().split()))

# 인접리스트 생성
adjL = list([] for _ in range(V+1))  # adjL = [[] for _ in range(V+1)]


