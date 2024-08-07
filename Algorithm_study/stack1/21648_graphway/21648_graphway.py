import sys
sys.stdin = open("input.txt", "r")


def DFS(vv):
    if vv == e_v:
        return 1
    visited[vv] = 1
    for next_vv in graph[vv]:
        if visited[next_vv] == 0:
            if DFS(next_vv):
                return 1
    return 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    for _ in range(E):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
    s_v, e_v = map(int, input().split())
    print(f'#{tc}', DFS(s_v))

