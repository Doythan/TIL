def build_tree(inorder, level_order, level):
    if not inorder:
        return

    mid = len(inorder) // 2
    level_order[level].append(inorder[mid])

    build_tree(inorder[:mid], level_order, level + 1)
    build_tree(inorder[mid + 1:], level_order, level + 1)


def solution():
    K = int(input())  # 트리의 깊이 K
    inorder = list(map(int, input().split()))  # 중위 순회 결과

    # 각 레벨별로 노드를 저장할 리스트 초기화
    level_order = [[] for _ in range(K)]

    # 트리 빌드 시작 (레벨 0부터)
    build_tree(inorder, level_order, 0)

    # 각 레벨별로 노드 출력
    for level in level_order:
        print(" ".join(map(str, level)))


# 예제 실행
solution()

