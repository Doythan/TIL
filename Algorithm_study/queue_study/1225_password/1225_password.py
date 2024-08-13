import sys
sys.stdin = open("input.txt", "r")

from collections import deque

for _ in range(10):
    tc = int(input())
    nums = list(map(int, input().split()))
    deque_nums = deque(nums)

    while deque_nums[7] != 0:
        for i in range(1, 6):
            if deque_nums[0] - i <= 0:
                deque_nums[0] = 0
            else:
                deque_nums[0] -= i
            deque_nums.append(deque_nums[0])
            deque_nums.popleft()
            if deque_nums[7] == 0:
                break

    # print(f'#{tc}', ' '.join(map(str, list(deque_nums))))
    print(f'#{tc}', *list(deque_nums))





