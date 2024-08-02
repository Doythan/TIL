# 셀렉션 알고리즘
# 자료로부터 k번째로 큰 혹은 작은 원소를 찾는 방법
# 자료 정렬 -> 원하는 순서에 있는 원소 가져오기
def select(arr, k):
    for i in range(0, k):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    print(arr[k-1])

a = [64, 25, 10, 22, 11]
select(a, 3)


