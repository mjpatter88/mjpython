def foo():
    return "foo"

def subtractor(a, b):
    return a - b

def summer(*args):
    return sum(args)

def summer_with_kw(*args, **kwargs):
    return sum(args) + sum(kwargs.values())

def calc(a, b, c):
    return subtractor(a, b) + subtractor(b, c)

print(foo())
print(subtractor(7, 5))
print(subtractor(a=7, b=5))
print(subtractor(b=7, a=5))
print(summer(1,2,3,4,5,6,7,8,9))
print(summer_with_kw(1,2,3,4,5, a=100, b=-5, c=70))
# print(calc(9, 4, 22))
