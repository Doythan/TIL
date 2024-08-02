import sys
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

for tc in range(1, 11):
    N = int(input())
    arr = [[0] * 102]
    arr += [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
    arr += [[0] * 102]
    left, right = 0, 0
    for i in range(100, -1, -1):
        if arr[100][i] == 2:
            j = i
    for i in range(len(arr)-3, 0, -1):
        while True:
            if arr[i][j-1] == 1 and right == 0:
                j -= 1
                left = 1
            elif arr[i][j+1] == 1 and left == 0:
                j += 1
                right = 1
            else:
                left, right = 0, 0
                break
    # print(j - 1)
    print(f'#{tc} {j - 1}')










