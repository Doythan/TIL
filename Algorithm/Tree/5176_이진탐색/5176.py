import sys
sys.stdin = open("input.txt", "r")


def in_order(node, tree, nums):  # 중위순회를 이용하여 트리를 만들기
    if node <= len(tree) - 1:
        in_order(node * 2, tree, nums)
        tree[node] = nums.pop(0)  # 트리에 중위순회로 값을 집어 넣기
        in_order(node * 2 + 1, tree, nums)


T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 노드 개수 입력
    tree = [0] * (N + 1)  # tree 인덱스는 완전 이진 트리의 노드 번호임
    nums = []  # 1 ~ N까지 숫자값
    for i in range(1, N + 1):
        nums.append(i)

    in_order(1, tree, nums)
    print(f'#{tc} {tree[1]} {tree[N // 2]}')


