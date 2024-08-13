import sys
sys.stdin = open("input.txt", "r")

from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # N : 화덕 크기, M : 피자 개수
    pizza = list(map(int, input().split()))  # 각각의 피자에 뿌려진 치즈의 양
    deque_pizza = deque(pizza)  # 피자 리스트를 덱큐로 변환
    fire_pot = deque()  # 피자를 넣을 화덕 덱큐로 변환
    check = deque()  # 현재 화덕(fire_pot)에 들어있는 피자가 몇 번째 피자인지 체크하기 위한 덱큐

    # 화덕 크기에 맞게 피자 투입 (초기 설정)
    for i in range(N):
        fire_pot.append(deque_pizza[i])
        check.append(i+1)

    cnt = 0  # 화덕에서 피자가 빠질 경우 남은 피자를 넣어 주기 위한 카운트(인덱스 계산에 사용)

    while len(fire_pot) != 1:  # 마지막 남은 피자
        fire_pot[0] //= 2
        if fire_pot[0] != 0:  # 치즈가 녹지 않았으면 그 피자 제일 뒤로 빼기
            fire_pot.append(fire_pot[0])
            check.append(check[0])
            fire_pot.popleft()
            check.popleft()
        elif fire_pot[0] == 0:  # 치즈가 다 녹으면 녹은 피자 뺴고, 다음 피자 투입 !
            fire_pot.popleft()
            check.popleft()
            if M - (M-N-cnt) < M:  # 화덕에 더 넣을 피자가 있으면 화덕에 피자 투입 !
                fire_pot.append(deque_pizza[M - (M-N-cnt)])
                cnt += 1
                check.append(N+cnt)

    print(f'#{tc}', check[0])





