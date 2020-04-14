def fib(n):
    a = 0
    b = 1
    while a < n:
        yield a
        tmp = a
        a = b
        b = tmp+b

for i in fib(10):
    print(i)