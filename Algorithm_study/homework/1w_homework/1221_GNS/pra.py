import sys
sys.stdin = open("input.txt", "r")

# # sol
# T = int(input())
# for _ in range(1, T+1):
#     tc, n = input().split()
#     words = input().split()
#     numbers = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
#     result = ""
#     for number in numbers:
#         for word in words:
#             if number == word:
#                 result += word + ' '
#     print(tc)
#     print(result)

# # sol 2
# T = int(input())
# for _ in range(1, T+1):
#     tc, n = input().split()
#     words = input().split()
#     str_to_number = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}
#     number_to_str = {0: 'ZRO', 1: 'ONE', 2: 'TWO', 3: 'THR', 4: 'FOR', 5: 'FIV', 6: 'SIX', 7: 'SVN', 8: 'EGT', 9: 'NIN'}
#     new_words = []
#     for word in words:
#         new_words.append(str_to_number[word])
#     new_words.sort()
#
#     result = []
#     for new_word in new_words:
#         result.append(number_to_str[new_word])
#     # print(' '.join(result))
#     print(*result)

# sol 3
numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
str_to_number = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}
T = int(input())
for _ in range(1, T+1):
    tc, n = input().split()
    words = input().split()
    max_value = 9
    count_list = [0] * (max_value + 1)
    for word in words:
        count_list[str_to_number[word]] += 1
    result = []
    for i, c in enumerate(count_list):
        result.extend([numbers[i]] * c)
    print(*result)

