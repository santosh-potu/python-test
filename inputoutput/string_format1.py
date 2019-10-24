year = 2016
event = 'Referendum'
print(f'Results of the {year} {event}')

yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)

print("{:-9} yes votes {:2.2%}".format(yes_votes,percentage))

s='Hello, world.'
print(str(s),' ',repr(s))
print(f"{s!r}")
import math
print(f"the value of pi is {math.pi:.3f}")


print('We are the {} who say "{}!"'.format('knights', 'Ni'))
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',other='Georg'))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Sjoerd:{0[Sjoerd]:d} Jack:{0[Jack]:d} Dcab:{0[Dcab]:d}'.format(table))
print('Sjoerd:{Sjoerd:d} Jack:{Jack:d} Dcab:{Dcab:d}'.format(**table))

for x in range (1,11):
    print("{0:2d} {1:3d} {2:4d}".format(x,x*x,x*x*x))




