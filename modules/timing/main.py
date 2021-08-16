import time
import timeit


def calc_time(func):
    def wrapper(*args, **kwargs):
        print('Executing', func.__name__)
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print('Elapsed time of', func.__name__, ':', elapsed_time)
    return wrapper


# @calc_time
def sum1(n):
    sum = 0
    for i in range(n):
        sum += i
    return sum


# @ calc_time
def sum2(n):
    return sum(range(n))


# sum1(300000000)
# sum2(300000000)

stmt = '''
sum1(1000)
'''
setup = '''
def sum1(n):
    sum = 0
    for i in range(n):
        sum += i
    return sum
'''

print(timeit.timeit(stmt, setup, number=100000))

stmt = '''
sum2(1000)
'''
setup = '''
def sum2(n):
    return sum(range(n))
'''
print(timeit.timeit(stmt, setup, number=100000))
