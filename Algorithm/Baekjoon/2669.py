arr_input = [list(map(int, input().split())) for _ in range(4)]

# N을 각 사각형의 최대 x, y 좌표를 통해 계산
max_x = max([rect[2] for rect in arr_input])
max_y = max([rect[3] for rect in arr_input])

# 2차원 배열을 초기화
arr = [[0] * (max_y + 1) for _ in range(max_x + 1)]

# 각 사각형의 범위에 해당하는 배열 요소를 1로 설정
for sq in range(4):
    for i in range(arr_input[sq][0], arr_input[sq][2]):
        for j in range(arr_input[sq][1], arr_input[sq][3]):
            arr[i][j] = 1

# 1로 설정된 요소의 개수를 카운트
cnt = 0
for i in range(max_x + 1):
    for j in range(max_y + 1):
        if arr[i][j] == 1:
            cnt += 1

print(cnt)
