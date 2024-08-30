def count_runways():
    pass


T = int(input())
for tc in range(1, T+1):
    N, X = map(int, input().split())
    ground = [list(map(int, input().split())) for _ in range(N)]

    count_runways(N, X, ground)
