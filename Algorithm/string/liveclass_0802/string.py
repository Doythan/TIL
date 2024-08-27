import sys
a = ''
b = 'a'
c = 'ab'
d = 'abc'

# 몇 바이트 쓰고 있는지
print(sys.getsizeof(a))
print(sys.getsizeof(b))
print(sys.getsizeof(c))
print(sys.getsizeof(d))

s = 'Reverse this strings'
s = s[::-1]
print(s)
s = ' abcd '
s = list(s)
print(s)
s.reverse()
print(s)