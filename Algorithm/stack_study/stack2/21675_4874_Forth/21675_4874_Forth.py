# import sys
# sys.stdin = open("input.txt", "r")


def calculator(calculation_formula):
    value_stack = []
    for char in calculation_formula:
        if char.isdecimal():
            value_stack.append(int(char))
        elif char == '.':
            if len(value_stack) == 1:
                return int(value_stack.pop())
            else:
                return 'error'
        else:
            if char == '.':
                break
            if len(value_stack) < 2:
                return "error"
            right = value_stack.pop()
            left = value_stack.pop()
            if char == '+':
                value_stack.append(left + right)
            elif char == '*':
                value_stack.append(left * right)
            elif char == '/':
                value_stack.append(int(left // right))
            elif char == '-':
                value_stack.append(left - right)
            # elif char == '.':
            #     if len(char) != 1:
            #         return "error"
            #         break
    return value_stack.pop()


T = int(input())
for tc in range(1, T + 1):
    calculation_formula = input().split()
    result = calculator(calculation_formula)
    print(f'#{tc}', result)



# def calculator(calculation_formula):
#     value_stack = []
#
#     for char in calculation_formula:
#         if char.isdecimal():
#             value_stack.append(int(char))
#         else:
#             if len(value_stack) < 2:
#                 return "error"
#             right = value_stack.pop()
#             left = value_stack.pop()
#
#             if char == '+':
#                 value_stack.append(left + right)
#             elif char == '*':
#                 value_stack.append(left * right)
#             elif char == '/':
#                 if right == 0:
#                     return "error"  # Division by zero error
#                 value_stack.append(left // right)
#             elif char == '-':
#                 value_stack.append(left - right)
#             else:
#                 return "error"  # Invalid operator error
#
#     if len(value_stack) != 1:
#         return "error"  # Invalid expression error
#
#     return value_stack.pop()
#
#
# T = int(input())
# for tc in range(1, T+1):
#     calculation_formula = input().split()
#     result = calculator(calculation_formula)
#     print(f'#{tc} {result}')
