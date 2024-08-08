def calculator_1(calculation_formula):
    prioritize = {'+': 1, '*': 2}  # 연산자 우선순위 check
    output_1 = []  # 후위 표기법으로 변환된 수식을 저장
    operator_stack = []  # 연산자를 저장할 스택
    for char in calculation_formula:
        if '0' <= char <= '9':
            output_1.append(char)
        elif char in prioritize:
            while operator_stack and prioritize[operator_stack[-1]] >= prioritize[char]:
                output_1.append(operator_stack.pop())
            operator_stack.append(char)
    while operator_stack:
        output_1.append(operator_stack.pop())
    return ''.join(output_1)


def calculator_2(calculation_formula):
    value_stack = []
    for char in calculation_formula:
        if '0' <= char <= '9':
            value_stack.append(int(char))
        else:
            if char == '+':
                value_stack.append(value_stack.pop() + value_stack.pop())
            elif char == '*':
                value_stack.append(value_stack.pop() + value_stack.pop())
    return value_stack.pop()


for tc in range(1):  # 테스트 케이스 10개
    n = int(input())  # 테스트 케이스의 길이 입력
    calculation_formula = input()  # 문자열 계산식 입력
    result_1 = calculator_1(calculation_formula)  # 후위표기법
    result_2 = calculator_2(result_1)  # 답
    print(result_2)

