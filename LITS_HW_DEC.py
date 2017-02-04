from decimal import*
class My_Zero_Division_Error(Exception):
    pass
class My_Type_Error(Exception):
    pass

def type_check(arg_type):
    def my_func(func):
        def wrapper(*args):
            if all([isinstance(arg,arg_type)for arg in args]):
                res = func(*args)
                return res
            else:
                raise My_Type_Error
        return wrapper
    return my_func

def my_dec4zero(func):
    def wrapper(x,y):
        if y == 0:
            raise My_Zero_Division_Error
        return func(x,y)
    return wrapper

@type_check((int,float,Decimal,str))
def summ(x,y):
    return x + y

@type_check((int,float,Decimal))
def sub(x,y):
    return x - y

@type_check((int,float,Decimal))
def mul(x,y):
    return x * y

@type_check((int,float,Decimal))
@my_dec4zero
def div(x,y):
    return x / y

print(summ('Hello ', 'World!'))
print(sub(2.477,1.478))
print(mul(Decimal(2.5),Decimal(2.5)))
print(div(Decimal(5),Decimal(5.5)))
