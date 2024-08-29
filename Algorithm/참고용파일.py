code_map = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}


def decode(code_str):
    numbers = []
    for i in range(0, len(code_str), 7):
        binary_str = code_str[i:i+7]
        if binary_str in code_map:
            numbers.append(code_map[binary_str])
    return numbers


def check_validity(numbers):
    odd_sum = sum(numbers[i] for i in range(0, 7, 2))
    even_sum = sum(numbers[i] for i in range(1, 7, 2))
    total = odd_sum * 3 + even_sum + numbers[7]
    return total % 10 == 0


def solve(N, M, data):
    for row in data:
        if '1' in row:  # 암호가 있는 줄을 찾음
            end = row.rfind('1')  # 마지막 '1'의 위치를 찾음
            start = end - 56 + 1  # 암호는 56자리이므로 시작 위치를 계산
            code_str = row[start:end+1]  # 암호를 추출
            decoded_numbers = decode(code_str)  # 이진수를 숫자로 변환
            if check_validity(decoded_numbers):  # 유효성 검사
                return sum(decoded_numbers)
    return 0  # 유효한 암호코드가 없는 경우 0 반환


# 메인 함수
for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    data = [input().strip() for _ in range(N)]
    answer = solve(N, M, data)
    print(f'#{tc} {answer}')
