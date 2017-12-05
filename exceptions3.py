#finally clause

def divide(x,y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("Division By zero!")
    else:
        print("Result is",result)
    finally:
        print("Executing finallly clause")

divide(2,1)
divide(2,0)
divide("2","1")

try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')



# clean code
with open('file1') as f:
    for line in f:
        print(line,end="")

try:
    raise NameError('Hi There')
except NameError:
    print('An exception flew by!')
    raise