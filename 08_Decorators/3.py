#implement a decorator that caches the return valuew of a function, so that when its called with the same argument , the cached value is returned instead of re-executing the function.
import time

def cache(func):
    cache_value={}
   
    def wrapper(*args,**kwargs):
        if args in cache_value:
            return cache_value[args]
        
        result = func(*args)
        cache_value[args] = result
        return result
        
        
        
    return wrapper


@cache
def long_running_function(a,b):
    time.sleep(5)
    return a+b

print(long_running_function(2,3))
# long_running_function(4,5)
print(long_running_function(2,3))
# long_running_function(4,5)
