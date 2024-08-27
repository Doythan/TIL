import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    C, N = input().split()
    str_list = list(map(str, input().split()))
    zro, one, two, thr, four, fiv, six, svn, egt, nin = [], [], [], [], [], [], [], [], [], []
    N = int(N)
    for i in range(N):
        if str_list[i] == 'ZRO':
            zro.append(str_list[i])
        elif str_list[i] == 'ONE':
            one.append(str_list[i])
        elif str_list[i] == 'TWO':
            two.append(str_list[i])
        elif str_list[i] == 'THR':
            thr.append(str_list[i])
        elif str_list[i] == 'FOR':
            four.append(str_list[i])
        elif str_list[i] == 'FIV':
            fiv.append(str_list[i])
        elif str_list[i] == 'SIX':
            six.append(str_list[i])
        elif str_list[i] == 'SVN':
            svn.append(str_list[i])
        elif str_list[i] == 'EGT':
            egt.append(str_list[i])
        elif str_list[i] == 'NIN':
            nin.append(str_list[i])
    ans = (zro + one + two + thr + four + fiv + six + svn + egt + nin)
    # print(f'#{tc}', *ans)
    print(f' #{tc}', " ".join(ans))
