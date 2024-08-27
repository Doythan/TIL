n = int(input())
a = list(map(int, input().split()))
start = 0
end = n - 1
b = sorted(a)
print(b)
# while start <= end:
#     middle = (start + end // 2)
#     if a[middle] == 19:
#         print(middle)
#         break
#     elif a[middle] > 19:
#         end = middle - 1
#     else:
#         start = middle + 1
