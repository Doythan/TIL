import sys
sys.stdin = open("input.txt", "r")

T = int(input())  # 노선 수 입력
for tc in range(1, T+1):
    K, N, M = map(int, input().split())  # K : 최대로 이동할 수 있는 정류장 수, N : 종점인 정류장 번호 M : 충전기가 설치된 정류장 갯수
    elec_busstop = list(map(int, input().split()))  # 충전기가 설치된 정류장 번호 리스트
    busstop = [0] * (N+1)  # 충전기가 설치된 정류장 체크를 위한 리스트
    current_idx = 0
    ans = 0

    # 충전기가 설치된 정류 1 입력
    for i in range(M):
        for j in range(N+1):
            if elec_busstop[i] == j:
                busstop[j] = 1

    while current_idx + K < N:
        cnt, cnt2 = 0, 0
        for i in range(current_idx + 1, current_idx + K + 1):
            if busstop[i] == 1:
                cnt += 1
        if cnt == 0:
            ans = 0
            break
        elif cnt == 1:
            ans += 1
            for j in range(current_idx + 1, current_idx + K + 1):
                if busstop[j] == 1:
                    current_idx = j
        elif cnt > 1:
            ans += 1
            for j in range(current_idx + 1, current_idx + K + 1):
                if busstop[j] == 1:
                    cnt2 += 1
                if cnt == cnt2:
                    current_idx = j
                    break
    print(f'#{tc}', ans)
