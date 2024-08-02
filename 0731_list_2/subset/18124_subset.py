arr = [1, 2, 3]
n = len(arr)
for i in range(1 << n):
    subset = []
    for j in range(n):
        if i & (1 << j):
            subset.append(arr[j])
    print(subset)

# T = int(input())
# for tc in range(1, T+1):
#     a = list(map(int, input().split()))
#     n = len(a)
#     ans = 0
#     for i in range(1 << n):
#         subset = []
#         for j in range(n):
#             if i & (1 << j):
#                 subset.append(a[j])
#             if subset and sum(subset) == 0:
#                 ans = 1
#                 break
#         if ans == 1:
#             break
#     print(f'#{tc} {ans}')
#
