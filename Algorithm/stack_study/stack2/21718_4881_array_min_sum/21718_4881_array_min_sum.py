import sys
sys.stdin = open("input.txt", "r")


def backtrack(row, current_sum):
    global min_sum  # 최솟값으로 저장할 변수, 전역 변수로 선언
    if row == n:  # 모든 행을 다 채운 경우
        if min_sum >= current_sum:  # 현재까지의 합이 min_sum 보다 작거나 같으면 min_sum을 갱신
            min_sum = current_sum
        return
    if min_sum < current_sum:  # 현재까지의 합이 이미 min_sum 보다 크면 더 이상 진행하지 않고 종료
        return
    for col in range(n):   # 현재 행에서 모든 열을 시도
        if visited[col] == 0:  # 해당 열이 방문 되지 않았을때
            visited[col] = 1  # 해당 열 방문 표시
            backtrack(row + 1, current_sum + arr[row][col])  # 다음 행으로 이동, 현재 합에 현재 위치 값 합함
            visited[col] = 0  # 열 방문 해제 (백트래킹)


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    current_sum = 0  # 현재 합 초기화
    visited = [0] * n  # 각 열 방문 여부를 저장하는 리스트 초기화
    min_sum = float('inf')  # 최솟값을 무한대로 초기화
    # for i in range(n):
    #     min_sum += arr[i][i]
    backtrack(row=0, current_sum=0)   # 백트래킹 함수 호출, 첫 번째 행부터 시작
    print(f"#{tc}", min_sum)
