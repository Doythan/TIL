# import sys
# sys.stdin = open("input.txt", "r")

for _ in range(10):
    tc = int(input())
    pattern = input()
    s_text = input()
    result = 0
    p_idx, c_idx = 0, 0
    while c_idx < len(s_text):
        if s_text[c_idx] != pattern[p_idx]:
            c_idx = c_idx - p_idx + 1
            p_idx = 0
        else:
            p_idx += 1
            c_idx += 1
        if p_idx == len(pattern):
            result += 1
            p_idx = 0
            c_idx = c_idx + 1
    print(f'#{tc} {result}')
