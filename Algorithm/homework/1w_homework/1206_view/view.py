for tc in range(1,11):
    N = int(input())
    arr = list(map(int, input().split()))
    answer = 0
    for i in range(2, N-1):
        if arr[i] > arr[i-1] and arr[i] > arr[i-2] and arr[i] > arr[i+1] and arr[i] > arr[i+2]:
            temp = 0
            for j in range(i-2, i+3):
                if arr[j] > temp and arr[j] != arr[i]:
                    temp = arr[j]
            answer += arr[i] - temp
    print(f'#{tc} {answer}')


