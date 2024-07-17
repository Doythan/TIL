# # greet 함수의 호출
# def greet(name):
#     message = 'Hello ' + name
#     return message
# result = greet('Alice')
# print(result)

def make_sum(pram1, pram2):
    """이것은 두 수를 받아
    두 수의 합을 반환하는 함수입니다.
    >>> make_sum(1, 2)
    3
    """
    return pram1 + pram2

result = make_sum(123, 321)
return_value = print(result) # return이 없다. return은 할당 가능, print 그냥 출력 따라서  return과 출력은 다른 함수
print(return_value)

def my_func():
    print('hello, world')
    
result = my_func()
print(result)