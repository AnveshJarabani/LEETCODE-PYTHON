def multiply_decorator(func):
    def wrapper(*args,**kwargs):
        print(f"function: {func.__name__}")
        print(f"args: {args}")
        print(f"kwargs: {kwargs}")
        result = func(*args,**kwargs)
        print(f"{func.__name__} with result: {result}")
        return result
    return wrapper


@multiply_decorator
def multiply(x,y,z=None,k=None):
    return x*y
x,y=5,5
result = multiply(x,y,z=5,k=10)
print(f"return: {result}")