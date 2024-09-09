def solution():
    t = int(input())  # 테스트 케이스 수 입력
    for _ in range(t):
        n, m = map(int, input().split())  # 국가 수 n, 비행기 수 m
        for _ in range(m):
            input()  # 비행기 정보는 무시 (단순히 간선의 개수만 세기 때문)
        print(n - 1)  # 최소 간선 수는 n-1

# 예제 실행
solution()
