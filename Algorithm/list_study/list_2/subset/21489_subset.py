# T = int(input())
# for tc in range(1, T+1):
#     q, p = int(input())
#     a = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10 ,11, 12]
#     n = len(a)
#     ans = 0
#     for i in range(1 << n):
#         subset = []
#         for j in range(n):
#             if i & (1 << j):
#                 subset.append(a[j])
#                 if len(subset) == q:
#                     if subset and sum(subset) == p:
#                         ans = 1
#                         break
#         if ans == 1:
#             break
#     print(f'#{tc} {ans}')

T = int(input())
for tc in range(1, T+1):
    q, p = map(int, input().split())
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    n = len(a)
    ans = 0
    for i in range(1 << n):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(a[j])
        if len(subset) == q and sum(subset) == p:
            ans += 1
    print(f'#{tc} {ans}')

