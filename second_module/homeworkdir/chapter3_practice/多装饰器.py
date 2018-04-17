
def document_it(func):
    def new_function(*args,**kwargs):
        print('Running function:',func.__name__)
        print('Positioal arguments:',args)
        print('keyword arguments:',kwargs)
        result = func(*args,**kwargs)
        print('document_is Result:',result)
        return result
    return new_function

def square_it(func):
    def another_new_function(*args,**kwargs):   #(3,6)
        result = func(*args,**kwargs)
        return result * result
    return another_new_function

@document_it
@square_it
def add_ints(a,b):
    return a+b

#
# @square_it
# @document_it
# def add_ints02(a,b):
#     return a+b

print('add_ints',add_ints(3,6))
# print('%s分割线%s'%('-'*10,'-'*10))
# print('add_ints02',add_ints(3,4))
