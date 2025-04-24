def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
        
print_kwargs(name="IronMan", power="Knowledge")
print_kwargs(name="Batman", power="Money" ,enemy="JOker")