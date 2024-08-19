import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())  # N : 자격 얻은 사람 수, M초의 시간을 들이면 K개의 빵을 만들 수 있음
    arrive_t = list(map(int, input().split()))  # N명의 사람이 각각 몇 초에 오는 지 입력
    arrive_t.sort()
    ans = 'Possible'
    time = M
    bung = K
    cnt = 0
    for i in range(N):
        if arrive_t[i] >= time:
            while True:
                if (time + M) < arrive_t[i]:
                    time += M
                    bung += K
                else:
                    break
            bung -= 1
            if bung < 0:
                ans = 'impossible'
                break

        elif arrive_t[i] < time:
            ans = 'Impossible'
            # bung -= 1
            # if bung < 0:
            #     ans = 'Impossible'

    print(f'#{tc}', ans)

    print(ans)
    