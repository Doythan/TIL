# from collections import deque
import sys
sys.stdin = open("input.txt", "r")


def dfs(n, a_list, b_list):
    global ans
    if n == N:
        if len(a_list) == M:  # a음식에 선택된 재료 개수가 절반일 경우
            a_sum, b_sum = 0, 0  # 음식맛의 합 구하기
            for i in range(M):
                for j in range(M):
                    a_sum += arr[a_list[i]][a_list[j]]
                    b_sum += arr[b_list[i]][b_list[j]]
            ans = min(ans, abs(a_sum - b_sum))
        return
    dfs(n + 1, a_list+[n], b_list)
    dfs(n + 1, a_list, b_list + [n])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = N // 2
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 20000 * N * N

    dfs(0, [], [])
    print(f'#{tc}', ans)
