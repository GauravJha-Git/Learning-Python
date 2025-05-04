#write a decorator that measures the time a function takes to execute
import time

def timer(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result = func(*args,**kwargs)
        end = time.time()
        
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper


@timer
def example_fun(n):
    time.sleep(n)
    
  
@timer  
def num(a,b):
    print(a+b)
    
example_fun(2)
num(5,6)