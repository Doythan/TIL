# 반복 문자 지우기

def remove_char(s):
    stack = []
    for char in string:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return len(stack)


T = int(input())
for tc in range(1, T+1):
    string = input()
    result = remove_char(string)
    print(f'#{tc}', result)








