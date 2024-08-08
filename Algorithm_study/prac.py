# a = '1abcd'
# a_l = list(a)
# for char in a_l:
#     if int(char):
#         print(char)
#     else:
#         print("알파벳")
#

a = '1abcd'
# a_l = list(a)

for char in a:
    # char이 숫자인지 확인
    if '0' <= char <= '9':
        print(char)
    else:
        print("알파벳")
