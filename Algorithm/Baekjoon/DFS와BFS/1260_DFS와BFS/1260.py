from collections import deque
import sys
sys.stdin = open("input.txt", "r")


def dfs(c):  # c : current
    ans_dfs.append(c)  # 방문 노드 추가
    v[c] = 1           # 방문 표시

    for n in adj[c]:
        if not v[n]:   # 방문하지 않은 노드인 경우
            dfs(n)


def bfs(s):  # s : start
    q = deque([])             # 필요한 q, v[], 변수 생성
    q.append(s)        # Q에 초기데이터(들) 삽입
    ans_bfs.append(s)
    v[s] = 1


    while q:
        c = q.popleft()
        for n in adj[c]:
            if not v[n]:  # 방문하지 않은 노드 => 큐 삽입
                q.append(n)
                ans_bfs.append(n)
                v[n] = 1


N, M, V = map(int, input().split())  # 정점의 개수, 간선의 개수, 탐색을 시작할 정점의 번호 입력
adj = [[] for _ in range(N+1)]  # 인접리스트 생성(인덱스 0은 사용X)
for _ in range(M):
    s, e = map(int, input().split())  # 간선이 연결하는 두 정점 입력
    # 양방향
    adj[s].append(e)
    adj[e].append(s)

# 오름차순 정렬
for i in range(1, N+1):
    adj[i].sort()

v = [0] * (N + 1)  # visted 배열 만들어줌(dfs 함수에서 사용)
ans_dfs = []
dfs(V)

v = [0] * (N + 1)  # visted 배열 만들어줌(bfs 함수에서 사용)
ans_bfs = []
bfs(V)

print(*ans_dfs)
print(*ans_bfs)

'''
[입력]
5 5 3
5 4
5 2
1 2
3 4
3 1
[출력]
3 1 2 5 4
3 1 4 2 5
'''