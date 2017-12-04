while True:
    try:
        x = int(input("Enter any number"))
        break;
    except ValueError:
        print("Oops ! thats not valid integer")


class B(Exception):
    pass


class C(B):
    pass


class D(C):
    pass


for cls in [B,C,D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")


import sys

try:
    f=open('file1')
    s=f.readline(f)
    i=int(s.strip())
except OSError as o:
    print("OS err {0}".format(0))
except ValueError:
    print("Cannot convert data into Integer")
except:
    print("Unexpected error: ",sys.exc_info()[0])
    raise




