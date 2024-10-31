array = [1, 2, 3,4,5,6]
#
# for num in array:
#     print(num)
# else:
#     print("else문이 실행되는가? ")


for num in array:
    print(num)
    if num == 3:
        continue
else:
    print("break를 하면 else문이 실행되는가? ")
