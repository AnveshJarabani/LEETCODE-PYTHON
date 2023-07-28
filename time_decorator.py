from time import time
import sys
sys.set_int_max_str_digits(500)
def timer(func):
    def wrapper(*args, **kwargs):
        start=time()
        print(f"started {func.__name__}")
        print(f"args: {args}")
        print(f"kwargs: {kwargs}")
        result=func(*args, **kwargs)
        print(f"Total time: {round(time()-start,2)} Seconds")
        print(f"result: {result}")
    return wrapper

@timer
def multiplier(x):
    result=1
    for i in range(1,x+1):
        result*=i
    return result
x=10

multiplier(x)
    