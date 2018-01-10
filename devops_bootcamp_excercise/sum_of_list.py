list1 = [ 4,49,23,55,4]
total = 0
max_num = list1[0]
for list_item in list1:
    total = total + list_item
    if(max_num<list_item):
        max_num = list_item

print ("Max element in the list is:",max_num," & ",end='')
print("Sum of list elements is:",total)

print ("Max element in the list is:",max(list1)," & ","Sum of list elements is:",sum(list1))
