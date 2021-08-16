def gen_fibo(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


x = gen_fibo(10)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

s = 'hello'
s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))

# for i in gen_fibo(100):
#     print(i)
