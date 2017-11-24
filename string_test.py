s = "hello , world"
print(str(s))
print(repr(s))

print(str(1/7))
print(repr(1/7))

x = 2.0/11.0
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)

s = 'The value of x is ' + str(x) + ', and y is ' + str(y) + '...'
print(s)

# The repr() of a string adds string quotes and backslashes:
hello = 'hello world\n'
hello = repr(hello)
print(hello)

print(repr((x,y,("spam",'eggs'))))

for x in range(1,11):
    print(repr(x).rjust(2),repr(x*x).rjust(3),end=' ')
    print(repr(x*x*x).rjust(4))


for x in range(1,11):
    print('{0:2d} {1:3d} {2:4d}'.format(x,x*x,x*x*x))

print('12'.zfill(5))
print('-3.14'.zfill(7))
print('3.14159265359'.zfill(5))

print('We are the {} who say ""'.format("Knights",'Ni!'))
print('{0} and {1}'.format('eggs','spam'))
print('{1} and {0}'.format('eggs','spam'))

print('This {food} is {adjective}'.format(food="Pizza",adjective="horribile"))
print("The story of {0},{1} and {other}".format('Santosh','Uma',other="Krishna"))

content = "Chess"
print('My favorite game is {}'.format(content))
print('My favorite game is {!r}'.format(content))

import math
print('The Actual value of PI approximately is {0:.3f}'.format(math.pi))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678,'':1,'t':0}
for name,phone in table.items():
    print('{0:10} ==> {1:10d}'.format(name,phone))


table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Sjoerd: {0[Sjoerd]:d}; Jack: {0[Jack]:d}; Dcab: {0[Dcab]:d};'.format(table))
print('Sjoerd: {Sjoerd:d}; Jack:{Jack}; Dcab:{Dcab};'.format(**table))

import math
print('The value of PI is approximately %5.3f '% math.pi)




