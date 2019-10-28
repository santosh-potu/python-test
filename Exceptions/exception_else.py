import sys
for arg in sys.argv[1:]:
    try:
        f = open(arg,'r')
    except OSError:
        print("Cannot open ",arg)
    else:
        print(arg, 'has', f.readlines(), ' Lines')
        f.close()