# 1. Positional Arguments(위치인자)
def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')
greet('Harry kane', 27)

# 2. Default Argument Values(기본 인자 값)
def greet(name, age=27):
    print(f'안녕하세요, {name}님! {age}살이시군요.')
greet('Harry kane')
greet('Sonny', 33)

# 3. Keyword Arguments(키워드 인자)
def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')
greet(name='Ben Davis', age=35)
greet(age=35, name='Ben Davis')

# 4. Arbitrary Argument Lists(임의의 인자 목록), args로 보통 씀
def calculate_sum(*args): 
    print(args)
    print(type(args))
    total = sum(args)
    print(f'합계: {total}')
calculate_sum(1, 2, 3)

# 5. Arbitrary Keyword Argument Lists(임의의 키워드 인자 목록), kwargs로 보통 씀 
def print_info(**kwargs):
    print(kwargs)
    print(type(kwargs))
print_info(name='Eve', age=30)

# 인자의 모든 종류를 적용한 예시
def func(pos1, pos2, default_arg='default', *args, **kwargs):
    print('pos1:', pos1)
    print('pos2:', pos2)
    print('default_arg:', default_arg)
    print('args:', args)
    print('kwargs:', kwargs)


func(1, 2, 3, 4, 5, 6, key1='value1', key2='value2')
