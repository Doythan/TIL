'''
7 8
1 3 1 2 2 4 2 5 4 6 5 6 6 7 3 7
,
[[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [6, 3]]
'''
def DFS(s, V):
    visited = [0] * (V+1)
    stack = []
    visited[s] = 1
    ans = [s]
    v = s
    while True:
        for w in sorted_graph[v]:
            if visited[w] == 0:
                stack.append(v)
                v = w
                ans.append(v)
                visited[w] = 1
                break
        else:
            if stack:
                v = stack.pop()
            else:
                break
    return "-".join(map(str, ans))


V, E = map(int, input().split())  # 정점의 개수 V와, 간선의 개수 E 입력
edges = list(map(int, input().split())) # 간선의 개수 만큼 연결된 두 정점
graph = [[] for _ in range(V+1)]
# for i in range(0, len(edges), 2):
#     graph[edges[i]].append(edges[i+1])
for i in range(E):
    v1, v2 = edges[i*2], edges[i*2+1]
    graph[v1].append(v2)
    graph[v2].append(v1)
sorted_graph = [sorted(row) for row in graph]

print(f'#{1}', DFS(1, V))











