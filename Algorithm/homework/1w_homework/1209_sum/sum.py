import sys
sys.stdin = open("../sum/input.txt", "r")

for tc in range(1, 11):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    max_row, max_column, temp_row, temp_column, dia_1, dia_2 = 0, 0, 0, 0, 0, 0
    anwser = 0
    for i in range(100):
        dia_2 += arr[i][99 - i]
        for j in range(100):
            temp_row += arr[i][j]
            temp_column += arr[j][i]
            if i == j:
                dia_1 += arr[i][j]
            if max_row < temp_row:
                max_row = temp_row
            if max_column < temp_column:
                max_column = temp_column
        temp_row, temp_column = 0, 0
    temp = [max_row, max_column, dia_1, dia_2]
    # anwser = max(temp)
    for i in range(4):
        if anwser < temp[i]:
            anwser = temp[i]
    print(f'#{tc} {anwser}')






