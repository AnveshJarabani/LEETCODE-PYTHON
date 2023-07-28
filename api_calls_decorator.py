from time import time
def rate_limit(period,max_call_count):
    def decorator(func):
        call_count=0
        last_call=time()
        def wrapper(*args, **kwargs):
            nonlocal call_count,last_call
            elapsed_time=time()-last_call
            if elapsed_time>period:
                call_count=0
                last_call=time.time()
            if call_count>=max_call_count:
                raise Exception("Rate Limit Exceeded. Please try again later")
            call_count+=1
            return func(*args, **kwargs)
        return wrapper
    return decorator


@rate_limit(period=10,max_call_count=6)
def api_call():
    print('API EXCEUTED SUCCESSFULLY')


for i in range(10):
    try:
        api_call()
    except Exception as e:
        print(f"EXCEPTION OCCURED: {e}")