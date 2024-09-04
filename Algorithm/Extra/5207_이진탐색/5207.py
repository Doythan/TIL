def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    last_direction = 0  # 0: 초기 상태, -1: 왼쪽, 1: 오른쪽

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return True

        elif arr[mid] < target:
            if last_direction == 1:
                return False  # 이미 오른쪽으로 간 경우, 중복된 탐색 방지
            left = mid + 1
            last_direction = 1

        else:
            if last_direction == -1:
                return False  # 이미 왼쪽으로 간 경우, 중복된 탐색 방지
            right = mid - 1
            last_direction = -1

    return False


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 배열 A의 크기, 배열 B의 크기 입력
    arr_a = list(map(int, input().split()))  # 배열 A 입력
    arr_a.sort()  # 배열 A 오름차순으로 정렬
    arr_b = list(map(int, input().split()))  # 배열 B 입력

    cnt = 0
    for i in range(len(arr_b)):
        if binary_search(arr_a, arr_b[i]):
            cnt += 1

    print(f'#{tc} {cnt}')





