# arr = ['O', 'X']
# path = []
# name = ['MIN', 'CO', 'TIM']
#
#
# def print_name():
#     print('{', end=' ')
#     for i in range(3):
#         if path[i] == 'O':
#             print(name[i], end=' ')
#     print('}')
#
#
# def run(lev):
#     if lev == 3:
#         print_name()
#         # print(path)
#         return
#
#     for i in range(2):
#         path.append(arr[i])
#         run(lev + 1)
#         path.pop()
#
#
# run(0)

# arr = ['A', 'B']
# n = len(arr)
#
#
# def get_sub(tar):
#     for i in range(n):
#         if tar & 1:
#             print(arr[i], end=' ')
#         tar >>= 1
#     return
#
#
# for tar in range(0, 1 << n):
#     print('{', end=' ')
#     get_sub(tar)
#     print('}')

arr = ['1', '2', '3', '4', '5', '6']
path = []
n = 3


def run(lev):
    if lev == 3:
        print(path)
        return

    for i in range(6):
        path.append(arr[i])
        run(lev + 1)
        path.pop()


run(0)