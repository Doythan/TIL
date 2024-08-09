def check_match(expression):
    stack = []
    matching_dict = {')': '(', '}': '{', ']': '['}
    for char in expression:
        if char in matching_dict.values():
            stack += [char]
        elif char in matching_dict.keys():
            if not stack or stack[-1] != matching_dict[char]:
                return False
            stack.pop()
    if len(stack) == 0:
        return True
    return False


T = int(input())
for tc in range(1, T+1):
    brackets = [input()]
    for bracket in brackets:
        if check_match(bracket):
            print(f'#{tc} {1}')
        else:
            print(f'#{tc} {-1}')


