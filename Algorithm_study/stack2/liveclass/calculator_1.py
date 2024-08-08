def infix_to_postfix(expression):
    # 연산자의 우선순위를 정의
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    output = []  # 후위 표기법으로 변환된 수식을 저장할 리스트
    operators = []  # 연산자를 저장할 스택

    for char in expression:
        if char.isnumeric():  # 피연산자인 경우
            output.append(char)  # 출력 리스트에 추가
        elif char in precedence:  # 연산자인 경우
            while operators and operators[-1] != '(' and precedence[operators[-1]] >= precedence[char]:
                output.append(operators.pop())  # 스택에서 연산자를 꺼내 출력 리스트에 추가
            operators.append(char)  # 현재 연산자를 스택에 추가
        elif char == '(':  # 여는 괄호인 경우
            operators.append(char)  # 스택에 추가
        elif char == ')':  # 닫는 괄호인 경우
            while operators and operators[-1] != '(':
                output.append(operators.pop())  # 여는 괄호를 만날 때까지 스택에서 연산자를 꺼내 출력 리스트에 추가
            operators.pop()  # 여는 괄호를 스택에서 제거

    while operators:  # 스택에 남아있는 모든 연산자를 출력 리스트에 추가
        output.append(operators.pop())

    return ''.join(output)  # 리스트를 문자열로 변환하여 반환


def evaluate_postfix(expression):
    stack = []  # 피연산자를 저장할 스택

    for char in expression:
        if char.isnumeric():  # 피연산자인 경우
            stack.append(int(char))  # 스택에 추가
        else:  # 연산자인 경우
            right = stack.pop()  # 오른쪽 피연산자를 스택에서 꺼냄
            left = stack.pop()  # 왼쪽 피연산자를 스택에서 꺼냄
            if char == '+':
                stack.append(left + right)  # 더한 결과를 스택에 추가
            elif char == '-':
                stack.append(left - right)  # 뺀 결과를 스택에 추가
            elif char == '*':
                stack.append(left * right)  # 곱한 결과를 스택에 추가
            elif char == '/':
                stack.append(left / right)  # 나눈 결과를 스택에 추가
            elif char == '^':
                stack.append(left ** right)  # 제곱한 결과를 스택에 추가

    return stack[0]  # 최종 결과를 반환

# 예제 사용
expression = "(6+5*(2-8)/2)"
postfix_expression = infix_to_postfix(expression)
print("후위 표기법:", postfix_expression)  # "3528-*+"
result = evaluate_postfix(postfix_expression)
print("계산 결과:", result)  # -25
