def dfs(index, current_result, plus, minus, multiply, divide):
    global max_result, min_result

    # 모든 숫자를 다 사용한 경우
    if index == N:
        max_result = max(max_result, current_result)
        min_result = min(min_result, current_result)
        return

    # 덧셈 연산자 사용 가능하면
    if plus > 0:
        dfs(index + 1, current_result + numbers[index], plus - 1, minus, multiply, divide)

    # 뺄셈 연산자 사용 가능하면
    if minus > 0:
        dfs(index + 1, current_result - numbers[index], plus, minus - 1, multiply, divide)

    # 곱셈 연산자 사용 가능하면
    if multiply > 0:
        dfs(index + 1, current_result * numbers[index], plus, minus, multiply - 1, divide)

    # 나눗셈 연산자 사용 가능하면
    if divide > 0:
        # 나눗셈은 음수일 때 주의해야 함
        if current_result < 0:
            dfs(index + 1, -(-current_result // numbers[index]), plus, minus, multiply, divide - 1)
        else:
            dfs(index + 1, current_result // numbers[index], plus, minus, multiply, divide - 1)


# 입력 받기
T = int(input())  # 테스트 케이스 수

for test_case in range(1, T + 1):
    N = int(input())  # 숫자의 개수
    operators = list(map(int, input().split()))  # 연산자의 개수 [+, -, *, /]
    numbers = list(map(int, input().split()))  # 사용할 숫자들

    # 최대값, 최소값 초기화
    max_result = -float('inf')
    min_result = float('inf')

    # 첫 번째 숫자를 가지고 dfs 시작
    dfs(1, numbers[0], operators[0], operators[1], operators[2], operators[3])

    # 결과 출력
    print(f"#{test_case} {max_result - min_result}")
