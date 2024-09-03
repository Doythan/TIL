import sys
sys.stdin = open("input.txt", "r")


T = int(input())
for tc in range(1, T+1):
    numbers, N = input().split()
    arr = []
    arr_copy = []
    cnt = 0
    idx = -1

    for i in range(len(numbers)):
        arr.append(int(numbers[i]))
        arr_copy.append(int(numbers[i]))

    # 입력받은 횟수만큼 교환할 때 까지 반복
    while cnt < int(N):
        max_v = max(arr_copy)
        if max_v != 0:
            for i in range(len(arr_copy)-1, -1, -1):
                if arr_copy[i] == max_v:
                    arr_copy[i] = 0
                    idx += 1
                    break
            for i in range(len(arr)-1, idx, -1):
                if arr[i] == max_v:
                    arr[i], arr[idx] = arr[idx], arr[i]
                    cnt += 1
                    if arr[idx] == arr[idx-1]:
                        if arr[i] < arr[i+1]:
                            arr[i], arr[i+1] = arr[i+1], arr[i]
                            break
                    else:
                        break

        elif max_v == 0 and arr != arr.sort(reverse=True):
            arr[len(arr)-1], arr[len(arr)-2] = arr[len(arr)-2], arr[len(arr)-1]
            cnt += 1

        elif max_v == 0 and arr == arr.sort(reverse=True):
            for i in range(len(arr)):
                for j in range(len(arr)):
                    if arr[i] == arr[j]:
                        cnt += 1
                        i = len(arr) - 1
                        break

    print(f'#{tc}', ''.join(map(str, arr)))

'''
12
123 1
2737 1
757148 1
78466 2
32888 2
777770 5
436659 2
431159 7
112233 3
456789 10
218888 3
218888 4
'''









