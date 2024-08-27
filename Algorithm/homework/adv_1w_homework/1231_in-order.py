import sys
sys.stdin = open("input.txt", "r")


def in_order(node):
    if node:
        in_order(left[node])  # 왼쪽 자식 방문
        print(tree_char[node], end='')  # 현재 노드 값 출력
        in_order(right[node])  # 오른쪽 자식 방문


for tc in range(1, 11):
    N = int(input())  # 트리가 갖는 정점의 총 수
    tree_char = [''] * (N+1)  # 해당 정점의 문자
    left = [0] * (N+1)  # 해당 정점의 왼쪽 자식
    right = [0] * (N+1)  # 해당 정점의 오른쪽 자식

    for i in range(1, N + 1):
        n_info = list(input().split())  # N줄에 걸친 각각의 정점의 정보
        tree_char[i] = n_info[1]

        if len(n_info) >= 3:  # 자식 노드가 1개 이상 있을 경우
            left[i] = int(n_info[2])
        if len(n_info) == 4:  # 자식 노드가 2개 있을 경우
            right[i] = int(n_info[3])

    print(f'#{tc}', end=' ')
    in_order(1)
    print()






