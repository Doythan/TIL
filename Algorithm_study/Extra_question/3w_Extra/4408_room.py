import sys
sys.stdin = open("input.txt", "r")

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     my_list = [0] * 201  # 방 번호의 범위가 1~200이므로 201 크기의 리스트 사용
#     for _ in range(N):
#         cur, aft = sorted(map(int, input().split()))
#         cur = (cur + 1) // 2  # 방 번호를 구간으로 변환
#         aft = (aft + 1) // 2  # 방 번호를 구간으로 변환
#         for i in range(cur, aft + 1):
#             my_list[i] += 1
#
#     print(f'#{tc} {max(my_list)}')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    my_list = [0] * 401
    for _ in range(N):
        cur, aft = sorted(map(int, input().split()))
        for i in range(cur, aft+1):
            my_list[i] += 1

    print(f'#{tc}', max(my_list))


# # 동선이 가장 많이 겹칠때의 수 = 문제를 해결하기위한 답의 하한선(아무리 못해도 해당 횟수 이상의 시간이 필요)
# # 가장 많이 겹치는 동선과 해당 동선에 안겹치는 대상을 다 빼버리면 언제나 최대로 겹치는 동선의 수가 1씩 낮아짐
# # 즉, 동선이 가장 많이 겹칠때의 수 = 정답
#
# for t in range(1, int(input()) + 1):
#     # 복도의 전체 길이
#     corridor = [0] * (200 + 1)
#
#     # 학생의 위치와 돌아가야하는 방 위치 받아오기
#     for _ in range(int(input())):
#         # 7 2 인 경우 start=2, end=7
#         start, end = sorted(map(int, input().split()))
#         # start=2, end=7 인 경우 range(1, 4+1)
#         for i in range((start + 1) // 2, ((end + 1) // 2) + 1):
#             # 학생이 지나가는 경로에 +1씩 더함
#             corridor[i] += 1
#
#     print(f'#{t} {max(corridor)}')





2 3 4 5
6 7 8 9


0 1 1 1 1 1 1 1 1