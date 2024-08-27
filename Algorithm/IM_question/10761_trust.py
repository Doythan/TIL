import sys
sys.stdin = open("input.txt", "r")

# T = int(input())
# for tc in range(1, T+1):
#     case = input().split()
#     N = int(case[0])  # 버튼의 개수
#     blue = []  # 블루 버튼 위치 기록 리스트
#     orange = []  # 오렌지 버튼 위치 기록 리스트
#     for i in range(1, N+1):
#         if case[2*i-1] == 'B':
#             blue.append(int(case[2*i]))
#         else:
#             orange.append(int(case[2*i]))
#     b_p, o_p = 1, 1  # 블루와 오렌지의 현재 위치
#     bi, oi = 0, 0  # 블루와 오렌지 리스트 인덱스
#     temp_t = 0
#     time = 0
#     for i in range(1, len(case), 2):
#         if case[i] == 'B':
#             temp_t = abs(blue[bi] - b_p) + 1  # 블루 버튼이 있는 위치로 가서 버튼을 누르기 까지 걸리는 시간
#             b_p = blue[bi]  # 변화된 블루 위치
#             bi += 1
#             if oi < len(orange):
#                 if orange[oi] - o_p <= temp_t:  # 블루 버튼이 있는 위치로 가서 버튼을 누를 때 이동할 수 있는 만큼 오렌지도 이동
#                     o_p = orange[oi]
#                 elif orange[oi] - o_p > temp_t:
#                     o_p += temp_t
#             time += temp_t
#             temp_t = 0
#         elif case[i] == 'O':
#             temp_t = abs(orange[oi] - o_p) + 1
#             o_p = orange[oi]
#             oi += 1
#             if bi < len(blue):
#                 if blue[bi] - b_p <= temp_t:
#                     b_p = blue[bi]
#                 elif blue[bi] - b_p > temp_t:
#                     b_p += temp_t
#             time += temp_t
#             temp_t = 0
#     print(f'#{tc}', time)

# T = int(input())  # 테스트 케이스의 수 입력
#
# for tc in range(1, T+1):
#     case = input().split()
#     N = int(case[0])  # 버튼의 개수
#
#     blue_positions = []  # 블루 로봇이 누를 버튼의 위치 리스트
#     orange_positions = []  # 오렌지 로봇이 누를 버튼의 위치 리스트
#     button_sequence = []  # (로봇, 버튼 위치) 쌍을 저장하는 리스트
#
#     for i in range(1, N+1):
#         robot = case[2*i-1]
#         position = int(case[2*i])
#         button_sequence.append((robot, position))
#         if robot == 'B':
#             blue_positions.append(position)
#         else:
#             orange_positions.append(position)
#
#     b_pos, o_pos = 1, 1  # 블루와 오렌지 로봇의 초기 위치
#     b_index, o_index = 0, 0  # 블루와 오렌지 로봇의 버튼 리스트 인덱스
#     time = 0
#
#     for robot, position in button_sequence:
#         if robot == 'B':  # 블루 로봇이 버튼을 눌러야 하는 경우
#             move_time = abs(position - b_pos) + 1  # 블루 로봇이 해당 버튼을 누르기까지 걸리는 시간
#             b_pos = position  # 블루 로봇의 새로운 위치 업데이트
#             b_index += 1
#
#             if o_index < len(orange_positions):
#                 # 오렌지 로봇이 이동할 수 있는 만큼 이동
#                 if abs(orange_positions[o_index] - o_pos) <= move_time:
#                     o_pos = orange_positions[o_index]
#                 else:
#                     # 오렌지 로봇이 목표 위치 방향으로 move_time 만큼 이동
#                     o_pos += move_time if orange_positions[o_index] > o_pos else -move_time
#
#             time += move_time
#
#         elif robot == 'O':  # 오렌지 로봇이 버튼을 눌러야 하는 경우
#             move_time = abs(position - o_pos) + 1  # 오렌지 로봇이 해당 버튼을 누르기까지 걸리는 시간
#             o_pos = position  # 오렌지 로봇의 새로운 위치 업데이트
#             o_index += 1
#
#             if b_index < len(blue_positions):
#                 # 블루 로봇이 이동할 수 있는 만큼 이동
#                 if abs(blue_positions[b_index] - b_pos) <= move_time:
#                     b_pos = blue_positions[b_index]
#                 else:
#                     # 블루 로봇이 목표 위치 방향으로 move_time 만큼 이동
#                     b_pos += move_time if blue_positions[b_index] > b_pos else -move_time
#
#             time += move_time
#
#     print(f'#{tc} {time}')

T = int(input())
for tc in range(1, T+1):
    case = input().split()
    N = int(case[0])  # 버튼의 개수

    blue = []  # 블루 버튼 위치 기록 리스트
    orange = []  # 오렌지 버튼 위치 기록 리스트

    # 버튼 위치를 각 로봇의 리스트에 저장
    for i in range(1, N+1):
        if case[2*i-1] == 'B':
            blue.append(int(case[2*i]))
        else:
            orange.append(int(case[2*i]))

    b_pos, o_pos = 1, 1  # 블루와 오렌지의 현재 위치
    b_idx, o_idx = 0, 0  # 블루와 오렌지 리스트 인덱스
    time = 0  # 총 시간 초기화

    # 버튼 누르기 순서를 기준으로 이동
    for i in range(1, N+1):
        if case[2*i-1] == 'B':  # 블루 로봇의 차례인 경우
            move_time = abs(blue[b_idx] - b_pos) + 1  # 블루 로봇의 이동 시간 계산
            b_pos = blue[b_idx]  # 블루 로봇의 새로운 위치 갱신
            b_idx += 1

            # 오렌지 로봇의 이동 처리
            if o_idx < len(orange):
                if abs(orange[o_idx] - o_pos) <= move_time:
                    o_pos = orange[o_idx]
                else:
                    o_pos += move_time if orange[o_idx] > o_pos else -move_time

            time += move_time  # 총 시간에 이동 시간 더하기

        elif case[2*i-1] == 'O':  # 오렌지 로봇의 차례인 경우
            move_time = abs(orange[o_idx] - o_pos) + 1  # 오렌지 로봇의 이동 시간 계산
            o_pos = orange[o_idx]  # 오렌지 로봇의 새로운 위치 갱신
            o_idx += 1

            # 블루 로봇의 이동 처리
            if b_idx < len(blue):
                if abs(blue[b_idx] - b_pos) <= move_time:
                    b_pos = blue[b_idx]
                else:
                    b_pos += move_time if blue[b_idx] > b_pos else -move_time

            time += move_time  # 총 시간에 이동 시간 더하기

    print(f'#{tc} {time}')  # 결과 출력












