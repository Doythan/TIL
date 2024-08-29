# 이진 트리 표현에 대하여 전위 순회, 중위 순회한 정점의 번호를 출력하는 코드

def pre_order(T):
    if T:
        print(T, end=' ')
        pre_order(left[T])
        pre_order(right[T])


def in_order(T):
    if T:
        in_order(left[T])
        print(T, end=' ')
        in_order(right[T])


N = int(input())  # 1번부터 N번까지인 정점
E = N - 1  # 간선의 수
arr = list(map(int, input().split()))

left = [0] * (N + 1)  # 부모를 인덱스로 왼쪽 자식번호 저장(인덱스 0은 사용 x)
right = [0] * (N + 1)  # 부모를 인덱스로 왼쪽 자식번호 저장(인덱스 0은 사용 x)
parent = [0] * (N + 1)  # 자식을 인덱스로 부모 저장


# 부모노드를 인덱스로 하여 왼쪽 자식은 left에 오른쪽 자식은 right에 넣음
for i in range(E):
    par, chi = arr[i * 2], arr[i * 2 + 1]
    if left[par] == 0:
        left[par] = chi
    else:
        right[par] = chi
    parent[chi] = par  # 자식을 인덱스로 부모를 저장

# 루트(뿌리)를 찾기
chi = N
while parent[chi] != 0:
    chi = parent[chi]
root = chi

print('전위 순회 :', end=' ')
pre_order(root)

print('\n중위 순회 :', end=' ')
in_order(root)

'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

