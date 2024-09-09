import sys
sys.stdin = open("input.txt", "r")


def dfs(people, prob):
    global max_prob

    if prob <= max_prob:
        return
    if people == N:  # 모든 일 할당 끝
        max_prob = prob
        return
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            dfs(people + 1, prob * arr[people][i] / 100)
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 사람의 수 입력
    arr = [list(map(int, input().split())) for _ in range(N)] # i번 사람이 j번 일을 할 때의 확률 2차원 리스트

    visited = [0] * N
    max_prob = 0   # 모든 일을 성공할 확률 중 최대 값

    dfs(0, 1)
    print(f'#{tc} {max_prob * 100:.6f}')

