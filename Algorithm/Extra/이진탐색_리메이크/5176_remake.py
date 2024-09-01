class tree:  # 트리 노드 클래스 정의
    def __init__(self, left=0, right=0):
        self.right = right  # 오른쪽 자식 노드 인덱스
        self.left = left    # 왼쪽 자식 노드 인덱스

    def data(self, d=0):
        self.d = d  # 노드에 저장될 데이터 값

def inorder(N):
    """트리의 인오더(inorder) 순회 함수
    - 왼쪽 자식, 현재 노드, 오른쪽 자식 순서로 순회합니다.
    """
    if t[N]:  # 현재 노드가 존재하는 경우
        global cnt
        if t[N].left:  # 왼쪽 자식이 존재하면 재귀 호출
            inorder(t[N].left)
        t[N].data(pwd[cnt])  # 현재 노드에 데이터를 저장
        cnt += 1  # 다음 데이터로 이동
        if t[N].right:  # 오른쪽 자식이 존재하면 재귀 호출
            inorder(t[N].right)

if __name__ == '__main__':
    for tc in range(1, int(input()) + 1):  # 테스트 케이스 수만큼 반복
        X, cnt = 8, 0  # 트리의 노드 개수(X)와 순회 인덱스(cnt) 초기화
        arr = input()  # 입력값: 첫 글자는 salt n, 나머지는 salting된 암호 (총 17글자)

        pwd = [0] * 8  # 디코딩된 암호를 저장할 리스트 초기화
        t = [0] * 9  # 트리 노드들을 저장할 리스트 초기화 (인덱스 1부터 사용)

        # 첫 글자를 n으로 설정하고 나머지 부분을 arr에 저장
        n, arr = int(arr[0]), arr[1:]

        # 8개의 암호 값을 디코딩
        for i in range(8):
            pwd[i] = '0x' + arr[2 * i:2 * (i + 1)]  # 각 암호 값을 16진수로 변환
            pwd[i] = int(pwd[i], 16)  # 16진수를 정수로 변환
            pwd[i] -= (n * (i + 1))  # salt n에 따라 값을 조정

        # 트리 구성: 각 노드의 왼쪽과 오른쪽 자식을 설정
        for i in range(1, X + 1):
            if (i * 2 + 1) <= X:  # 왼쪽, 오른쪽 자식이 모두 있는 경우
                t[i] = tree(i * 2, i * 2 + 1)
            elif (i * 2) == X:  # 왼쪽 자식만 있는 경우
                t[i] = tree(i * 2)
            else:  # 자식이 없는 경우
                t[i] = tree()

        # 인오더 순회를 통해 트리에 디코딩된 암호 값을 할당
        inorder(1)

        # 결과 출력: 트리의 각 노드에 저장된 값을 10으로 나눈 나머지로 출력
        for x in range(X):
            pwd[x] = str(t[x + 1].d % 10)
        print(f'#{tc} ', *pwd, sep='')
