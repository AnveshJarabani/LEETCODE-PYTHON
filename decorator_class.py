def class_type(func):
    def wrapper(*args, **kwargs):
        result=func(*args, **kwargs)
        print(result)
        print(f"class: {type(result)}")
        return result
    return wrapper
@class_type
def string_concat(x,y):
    return x+" "+ y
x,y='abc','xyz'
string_concat(x,y)