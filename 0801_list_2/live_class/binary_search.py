# # 이진검색
# def binary_search(a, n, key):
#     start = 0
#     end = n - 1
#     while start <= end:
#         middle = (start + end) // 2
#         if a[middle] == key:
#             return True
#         elif a[middle] > key:
#             end = middle - 1
#         else:
#             start = middle + 1
#     return False
#
#
# arr = [2, 4, 7, 9, 11, 19, 23]
#
# if binarysearch(arr, len(arr), 23):
#     print("Key found")
# else:
#     print("Key not found")


# 이진검색 재귀로 풀기
def binarysearch2(a, low, high, key):
    if low > high:  # 검색실패
        return False
    else:
        middle = (low + high) // 2
        if key == a[middle]: # 검색 성공
            return True
        elif key < a[middle]:
            return binarysearch2(a, low, middle - 1, key)
        elif key > a[middle]:
            return binarysearch2(a, middle + 1, high, key)


arr = [2, 4, 7, 9, 11, 19, 23]

if binarysearch2(arr, 0, len(arr)-1, 22):
    print("Key found")
else:
    print("Key not found")

























