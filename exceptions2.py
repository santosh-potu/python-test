import sys
for arg in sys.argv[1:]:
    try:
        f = open(arg,'r')
    except OSError:
        print('cannot open ',arg)
    else:
        print(arg,' has ',len(f.readlines()),' lines')
        f.close()

try:
    raise Exception('spam','eggs')
except Exception as inst:
    print(type(inst))
    print(inst.args)
    print(inst)

    x, y = inst.args
    print('x = ',x)
    print('y = ',y)

def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as err:
    print("handling runtime error:",err)





