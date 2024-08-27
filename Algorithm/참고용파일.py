def inorder(node, tree, values):
    if node <= len(tree) - 1:
        inorder(node * 2, tree, values)  # 왼쪽 자식 노드 방문
        tree[node] = values.pop(0)  # 현재 노드에 값 할당
        inorder(node * 2 + 1, tree, values)  # 오른쪽 자식 노드 방문


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    tree = [0] * (N + 1)  # 이진 트리를 1부터 N까지 사용하도록 설정
    values = list(range(1, N + 1))  # 1부터 N까지의 값을 미리 준비

    inorder(1, tree, values)  # 중위 순회를 통해 트리를 구성

    print(f"#{t} {tree[1]} {tree[N // 2]}")
