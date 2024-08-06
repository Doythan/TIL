# # 스택 구현, 3개의 데이터를 스택에 저장하고 다시 3번 꺼내서 출력해 보기
#
# my_stack = []
# my_stack.append(1)  # push(1)
# my_stack.append(2)  # push(2)
# my_stack.append(3)  # push(3)
#
# print(my_stack.pop())
# print(my_stack.pop())
# print(my_stack.pop())

stack_size = 10
stack = [0] * stack_size
top = -1

top += 1
stack[top] = 1
top += 1
stack[top] = 2
top += 1
stack[top] = 3

top -= 1
print(stack[top+1])
print(stack[top])
top -= 1
print(stack[top])
top -= 1

# 스택의 응용1 : 괄호 검사
# 스택의 응용2 : function call


def f2(c, d):
    return c-d


def f1(a, b):
    c = a + b
    d = 10
    return f2(c, d)


a = 10
b = 20
print(f1(a, b))


