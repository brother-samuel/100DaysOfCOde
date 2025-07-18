def add(*args):
    summa = 0
    for n in args:
        summa += n
    return summa

print(add(2, 4, 12, 7))

def calculate(n, **kwargs):
    n += kwargs['add']
    n *= kwargs['multiply']
    return n

print(calculate(3, add=3, multiply=7))

