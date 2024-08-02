import sys
sys.stdin = open("input.txt", "r")

T = int(input())
value = 5
for tc in range(1, T+1):
    temp = []
    length = 0
    j = 0
    arr = [list(input()) for _ in range(value)]
    for i in range(value):
        if len(arr[i]) > length:
            length = len(arr[i])
    for j in range(length):
        for i in range(value):
            # print(arr[i])
            if j < len(arr[i]):
                temp += arr[i][j]
    print(f'#{tc}', ''.join(temp))




