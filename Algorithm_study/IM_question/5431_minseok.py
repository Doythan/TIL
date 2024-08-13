import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())  # N : 수강생 수, K : 과제를 제출한 사람의 수
    pass_stu = list(map(int, input().split()))  # 과제 제출한 학생 번호들
    ans = []
    for i in range(1, N+1):
        ans.append(i)
    for i in range(N):
        for j in range(K):
            if ans[i] == pass_stu[j]:
                ans[i] = 0
    print(f'#{tc}', end = ' ')
    for i in range(N):
        if ans[i] != 0:
            print(ans[i], end = ' ')
    print()







