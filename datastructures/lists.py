fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

print(fruits.count('apple'))
print(fruits.count('tangerine'))
print(fruits.index('banana'))
print(fruits.index('banana', 4))
fruits.reverse()
print(fruits)

fruits.append('grape')
fruits.sort()
print(fruits)
print(fruits.pop())

from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
print(queue.popleft())                 # The first to arrive now leaves
print(queue.popleft())                 # The second to arrive now leaves
print(queue)

vec = [-4, -2, 0, 2, 4]
print([x**2 for x in vec])
print([x for x in vec if x >=0 ])
print([abs(x) for x in vec])
print([(x,x**2) for x in range(6)])

vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for ele in vec for num in ele])
matrix = [
   [1, 2, 3, 4],
   [5, 6, 7, 8],
   [9, 10, 11, 12],
 ]

print([[row[i] for row in matrix] for i in range(4)])

transposed = []
for i in range(4):
     transposed.append([row[i] for row in matrix])

print(transposed)
