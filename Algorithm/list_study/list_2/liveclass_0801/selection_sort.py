# def selectionsort(a, n):
#     for i in range(n-1):
#         min_idx = i
#         for j in range(i+1, n):
#             if a[min_idx] > a[j]:
#                 min_idx = j
#         a[i], a[min_idx] = a[min_idx], a[i]
#     print(a)
#
#
# a = [64, 25, 10, 22, 11]
# selectionsort(a, len(a))

n = int(input())
a = list(map(int, input().split()))
for i in range(n-1):
    min_idx = i
    for j in range(i+1, n):
        if a[min_idx] > a[j]:
            min_idx = j
    a[i], a[min_idx] = a[min_idx], a[i]
print(a)
