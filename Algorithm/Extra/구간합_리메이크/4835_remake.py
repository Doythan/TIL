import sys
sys.stdin = open("input.txt", "r")


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr, section_length = [], []
    for _ in range(N):
        section = list(map(int, input().split()))
        arr.append(section)
        section_length.append(len(section))

    max_v, min_v = float('-inf'), float('inf')
    for j in range(max(section_length)):
        for i in range(N):
            temp, cnt = 0, 0
            for ii in range(i, N):
                if j >= section_length[ii]:
                    continue
                temp += arr[ii][j]
                cnt += 1
                if cnt == M:
                    if temp > max_v:
                        max_v = temp
                    if temp < min_v:
                        min_v = temp
    if N < M:
        print(f'#{tc}', -1)
        break
    print(f'#{tc}', max_v - min_v)



