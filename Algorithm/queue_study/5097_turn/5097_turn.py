import sys
sys.stdin = open("input.txt", "r")

#  queue 구현을 위해 deque 라이브러리 사용
from collections import deque
nums = deque()
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    deque_nums = deque(nums)  # 리스트 객체에는 'popleft' 메서드가 없기 때문에 리스트를 deque로 변환하여 사용

    for i in range(M):
        deque_nums.append(deque_nums[0])
        deque_nums.popleft()
    print(f'#{tc}', deque_nums[0])







