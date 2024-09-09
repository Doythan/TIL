import sys
sys.stdin = open("input.txt", "r")


def F(idx, current_probablity):
    global max_probablity

    if current_probablity <= max_probablity:  # 현재 확률이 최대 확률보다 작으면 백트래킹
        return
    if idx == N:  # 모든 일 할당 끝낸 경우
        max_probablity = current_probablity
        return
    for i in range(N):
        if not visited[i]:  # i번째 일이 아직 할당되지 않은 경우
            visited[i] = True
            F(idx + 1, current_probablity * probablity[idx][i] / 100)
            visited[i] = False


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    probablity = [list(map(int, input().split())) for _ in range(N)]

    visited = [False] * N
    max_probablity = 0
    F(0, 1)

    print(f'#{tc} {max_probablity * 100:.6f}')


