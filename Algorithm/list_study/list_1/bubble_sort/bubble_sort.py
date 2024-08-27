import sys
sys.stdin = open("input.txt", "r")
# sol1


def bubblesort(a, N):
    for i in range(N-1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a


N = int(input())
arr = list(map(int, input().split()))
bubblesort(arr, N)
print(arr)



# # sol2
# N = 6
# arr = [7, 2, 5, 3, 4, 1]
#
# for i in range(N-1, 0, -1):
#     for j in range(i):
#         if arr[j] > arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]
# print(*arr)