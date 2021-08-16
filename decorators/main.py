def return_decorator(func):
    def wrapper():
        print('=' * 10)
        func()
        print('=' * 10)
    return wrapper


@return_decorator
def func_needs_decorator():
    print("hello i'm stupid")


func_needs_decorator()
