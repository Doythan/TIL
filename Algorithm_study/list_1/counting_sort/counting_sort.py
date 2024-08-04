# # 내가 푼 거
# N = 8
# data = [0, 4, 1, 3, 1, 2, 4, 1]
# temp = [0] * N
# counts = [0] * (4+1)  # data 0~4 까지의 정수
# for i in range(N):
#     counts[data[i]] += 1
# print(counts)  # [1, 3, 1, 1, 2, 0, 0, 0, 0]
# for i in range(1, 4+1):
#     counts[i] += counts[i-1]
# print(counts)  # [1, 4, 5, 6, 8, 8, 8, 8, 8]
# for i in range(N-1, -1, -1):
#     counts[data[i]] -= 1
#     temp[counts[data[i]]] = data[i]
# print(*temp)

# 강사님 푼 거
data = [0, 4, 1, 3, 1, 2, 4, 1]
counts = [0] * 5 # data가 0~4까지의 정수
N = len(data) # 정렬 결과 저장
temp = [0] * N
# 1단계 : data 원소 별 개수 세기
for x in data: # data의 원소 x르 자져와서 counts[x]에 개수 기록
    counts[x] += 1
# 2단계 : 각 숫자까지의 누적 개수 구하기
for i in range(1, 5):
    counts[i] = counts[i-1] + counts[i]

# 3단계 : data의 맨 뒤부터
for i in range(N-1, -1, -1):
    counts[data[i]] -= 1
    temp[counts[data[i]]] = data[i]
print(temp)
