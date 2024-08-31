# 이진탐색

def in_order(node, tree, nums):
    if node <= len(tree) - 1:
        in_order(node * 2, tree, nums)
        tree[node] = nums.pop(0)
        in_order(node * 2 + 1, tree, nums)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N + 1)
    nums = []
    for i in range(1, N+1):
        nums.append(i)

    in_order(1, tree, nums)
    print(f'#{tc}', tree[1], tree[N//2])


