def dfs(idx, current_prob):
    global max_prob

    if current_prob <= max_prob:
        return

    if idx == N:
        max_prob = current_prob
        return

    for i in range(N):
        if not visted[i]:
            visted[i] = True
            dfs(idx + 1, current_prob * prob[idx][i] / 100)
            visted[i] = False


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    prob = [list(map(int, input().split())) for _ in range(N)]

    visted = [False] * N
    max_prob = 0
    dfs(0, 1)

    print(max_prob * 100)