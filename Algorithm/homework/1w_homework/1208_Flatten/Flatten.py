import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, 11):
    T = int(input())
    a = list(map(int, input().split()))
    new_a = sorted(a, reverse=True)
    for t in range(T):
        for i in range(len(new_a)+1):
            if new_a[i] > new_a[i+1]:
                new_a[i] -= 1
                break
        for j in range(len(new_a)-1, -1, -1):
            if new_a[j] < new_a[j-1]:
                new_a[j] += 1
                break
    # print(new_a)
    print(f'#{tc} {new_a[0] - new_a[len(new_a)-1]}')


