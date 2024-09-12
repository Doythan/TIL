import heapq

# 방향을 나타내는 4가지 움직임: 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dijkstra_min_cost(grid):
    n = len(grid)

    # 최소 비용을 저장할 테이블 (최대값으로 초기화)
    cost = [[float('inf')] * n for _ in range(n)]
    cost[0][0] = 0  # 출발점 비용은 0

    # 우선순위 큐 (cost, x좌표, y좌표) - 최소 비용 기준으로 정렬됨
    pq = [(0, 0, 0)]  # (비용, x좌표, y좌표)

    while pq:
        current_cost, x, y = heapq.heappop(pq)

        # 현재 위치가 이미 처리된 최소 비용보다 크면 무시
        if current_cost > cost[x][y]:
            continue

        # 현재 위치에서 4방향으로 이동
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 범위를 벗어나지 않으면
            if 0 <= nx < n and 0 <= ny < n:
                # 인접 지역으로 이동 가능하기 때문 비용 1 증가
                next_cost = 1 + current_cost
                # 더 높은 곳으로 이동하는 경우
                if grid[x][y] < grid[nx][ny]:
                    # 높이 차이만큼 비용 증가시킴
                    next_cost += grid[nx][ny] - grid[x][y]

                # 새로운 위치의 비용이 현재까지 계산한 최소 비용보다 작으면 갱신
                if next_cost < cost[nx][ny]:
                    cost[nx][ny] = next_cost
                    heapq.heappush(pq, (next_cost, nx, ny))

    # 목표 지점까지의 최소 비용 반환
    return cost[n - 1][n - 1]


# 테스트케이스
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]

    print(f'#{tc}', dijkstra_min_cost(grid))

'''
입출력 예제 
1
3
0 2 1
0 1 1
1 1 1

#1 5
'''
