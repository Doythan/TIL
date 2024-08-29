import sys
sys.stdin = open("input.txt", "r")


def postorder(node_num):
    # 현재 노드가 리프 노드(자식이 없는 경우)라면, 그 노드의 값을 반환
    if not tree[node_num]:
        return int(par_node[node_num])

    # 왼쪽 자식과 오른쪽 자식을 후위 순회 방식으로 재귀적으로 방문
    left = postorder(tree[node_num][0])
    right = postorder(tree[node_num][1])

    # 현재 노드의 연산자에 따라 왼쪽과 오른쪽 자식 노드의 값을 연산
    if par_node[node_num] == '+':
        return left + right
    elif par_node[node_num] == '-':
        return left - right
    elif par_node[node_num] == '*':
        return left * right
    elif par_node[node_num] == '/':
        return left / right


# 총 10개의 테스트 케이스를 처리
for tc in range(1, 11):
    # 트리의 노드 수를 입력받음
    N = int(input())

    # 각 노드의 연산자 또는 값을 저장하는 리스트 (1번 인덱스부터 사용)
    par_node = [''] * (N + 1)

    # 트리 구조를 저장하는 리스트, 각 노드는 두 자식을 가질 수 있음 (1번 인덱스부터 사용)

    tree = [[] for _ in range(N + 1)]

    # N개의 노드에 대한 정보를 입력받아 트리와 노드 정보 구성
    for _ in range(N):
        arr = list(input().split())
        node_num = int(arr[0])  # 현재 노드 번호
        par_node[node_num] = arr[1]  # 노드의 연산자 또는 값을 저장

        # 자식 노드가 있는 경우 트리 구조에 자식 노드 정보 추가
        if len(arr) == 4:
            tree[node_num].append(int(arr[2]))  # 왼쪽 자식
            tree[node_num].append(int(arr[3]))  # 오른쪽 자식

    # 후위 순회를 통해 루트 노드(1번 노드)부터 계산을 시작하여 결과를 얻음
    answer = int(postorder(1))

    # 각 테스트 케이스의 결과를 출력
    print(f'#{tc}', answer)

'''
5
1 - 2 3
2 - 4 5
3 10
4 88
5 65
'''






