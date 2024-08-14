T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # crop = list(input() for _ in range(N))
    # crop_list = []
    # crop_list = list([int(char) for char in i] for i in crop)
    crop = [list(map(int, input())) for _ in range(N)]
    print(crop)