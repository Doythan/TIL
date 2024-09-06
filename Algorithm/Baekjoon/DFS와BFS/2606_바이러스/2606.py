import sys
sys.stdin = open("input.txt", "r")


def dfs(c):  # c : current
    v[c] = 1

    for n in adj[c]:
        if not v[n]:
            dfs(n)


def virus_computer(v):
    cnt = 0
    for i in range(len(v)):
        if v[i] == 1:
            cnt += 1
    return cnt - 1


N = int(input())  # 컴퓨터 수 입력
M = int(input())  # 컴퓨터 쌍의 수
adj = [[] for _ in range(N + 1)]  # 인접리스트 입력
for _ in range(M):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

v = [0] * (N + 1)  # visted 배열 생성
dfs(1)
print(virus_computer(v))
