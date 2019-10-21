def concat(*args, sep="/"):
    return sep.join(args)


print(concat("earth", "mars", "venus", sep="."))


def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d =  {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}

print(parrot(**d))

def my_function():
    """Do nothing, but document it.

     No, really, it doesn't do anything.
    """
    pass

print(my_function.__doc__)


def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs


print(f('spam'))