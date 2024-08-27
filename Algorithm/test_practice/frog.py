import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    pond = [0] + list(map(int, input().split()))  # 인덱스 생각하기 편하게 0번째 인덱스에 제로 패딩
    frog = 1  # 현재 개구리 위치, 최종 개구리 위치 출력값
    while frog < N - K + 1:
        cnt = 0
        for i in range(frog + 1, frog + K + 1):
            if pond[i] == 1:  # 개구리가 점프 가능 범위 내에서의 연꽃 발견 시
                cnt += 1  # 카운트 1
                n_frog = i  # 다음 개구리 위치를 임시 저장
        frog = n_frog  # 개구리가 점프 가능 범위 내에서 개구리 위치 최신화(연꽃 2개 이상 시 멀리 떨어진 연꽃 위치로 최신화)
        if cnt == 0:  # 점프 가능 범위내에 연꽃이 없을 경우
            if frog + K <= N:  # 범위 길이가 넘지 않는 선에서
                frog += K  # 개구리가 최종 위치에서 점프 값으로 최신화
            break
    print(f'#{tc}', frog)






