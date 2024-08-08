import sys
sys.stdin = open("input.txt", "r")


def calculator(calculation_formula):
    output = []
    for char in calculation_formula:
        if '0' <= char <= '9':
            output.append(int(char))
    while True:
        output.append(output.pop() + output.pop())
        if len(output) == 1:
            break
    return output.pop()


for tc in range(1, 11):
    n = int(input())
    calculation_formula = input()
    result = calculator(calculation_formula)
    print(f'#{tc}', result)



