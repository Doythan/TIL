T = int(input())
for tc in range(1, T+1):
    string = input()
    n_string = string[::-1]
    if string == n_string:
        print(f'#{tc}', 1)
    else:
        print(f'#{tc}', 0)
