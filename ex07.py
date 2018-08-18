def foo():
   bar()

def bar():
    foo()
try:
    foo()
except RecursionError as error:
    print(error)
    print('there was an error')