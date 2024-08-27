import sys
sys.stdin = open("../5176_이진탐색/input.txt", "r")


def subtree(node):
    # 노드가 존재하지 않으면
    if node == 0:
        return 0
    # 현재 노드를 포함한 서브트리 노드 수 계산
    return 1 + subtree(left[node]) + subtree(right[node])


T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())  # 간선의 수, 서브트리의 루트 노드 N 입력
    pair = list(map(int, input().split()))

    left = [0] * (E + 2)   # 왼쪽 자식 노드 저장(부모를 인덱스로)
    right = [0] * (E + 2)  # 오른쪽 자식 노드 저장(부모를 인덱스로)

    for i in range(E):
        p, c = pair[i*2], pair[i*2+1]
        if left[p] == 0:  # 왼쪽 자식이 없으면
            left[p] = c   # + 왼쪽 자식
        else:             # 왼쪽 자식이 있으면
            right[p] = c  # + 오른쪽 자식

    result = subtree(N)
    print(f'#{tc}', result)

