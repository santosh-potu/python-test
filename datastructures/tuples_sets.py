t = 12345, 54321, 'hello!'
print(t[0])
print(t)
(12345, 54321, 'hello!')
# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print(u)

empty = ()
singleton = 'hello',    # <-- note trailing comma
print(len(empty))
print(len(singleton))

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed
# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')
print(a)                                  # unique letters in a
print(a - b)                              # letters in a but not in b
print(a | b)                              # letters in a or b or both
print(a & b)                              # letters in both a and b
print(a ^ b)                              # letters in a or b but not both
