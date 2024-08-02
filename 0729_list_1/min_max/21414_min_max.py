'''
입력 예제 )
3
5
477162 658880 751280 927930 297191
5
565469 851600 460874 148692 111090
10
784386 279993 982220 996285 614710 992232 195265 359810 919192 158175
'''
# # sol 1
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     max_value = arr[0]
#     min_value = arr[0]
#     for a in arr:
#         if max_value < a:
#             max_value = a
#         if min_value > a:
#             min_value = a
#     print(f'#{tc} {max_value - min_value}')

# sol 2
T = int(input()) # 테스트 케이스 개수
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_v = arr[0]
    min_v = arr[0]
    for i in range(1, N):
        if max_v < arr[i]:
            max_v = arr[i]
    for i in range(1, N):
        if min_v > arr[i]:
            min_v = arr[i]
    print(f'#{tc} {max_v-min_v}')