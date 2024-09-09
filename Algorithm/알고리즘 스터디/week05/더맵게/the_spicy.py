import heapq


def solution(scoville, K):
    heapq.heapify(scoville)  # 스코빌 리스트를 최소 힙으로 변환
    mix_count = 0

    while scoville[0] < K:  # 가장 작은 스코빌 지수가 K 이상이 될 때까지 반복
        if len(scoville) < 2:  # 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우
            return -1

        # 가장 작은 두 개의 음식 섞기
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        new_scoville = first + (second * 2)
        heapq.heappush(scoville, new_scoville)
        mix_count += 1

    return mix_count


# 예시
scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville, K))  # 출력: 2
