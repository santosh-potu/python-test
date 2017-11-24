t = open('file1','w')
t.write('')
t.close() # make empty file

with open('file1','a') as f1:
    for number in range(1,11):
        if number < 11:
            f1.write('This is Line {0}\n'.format(number))
        else:
            f1.write('\n') #To test file end as \n


f1 = open('file1') # default read r
print(f1.read()) #entire file

f1.seek(0,0) # goto begining

line = f1.readline()
while line :
    print("Line from file ->",line)
    line = f1.readline()

f1.seek(0,0) # goto begining
for lin in f1:
    print(lin,end='')

f1.close()

f2 = open('file2','w+')
value = ('the answer', 42)
s = str(value)  # convert the tuple to string
print('write operation result',f2.write(s))
f2.seek(0,0)
print(f2.read())
print('End of the file offset',f2.tell())
f2.close()

#binary file
f = open('workfile', 'wb+')
print(f.write(b'0123456789abcdef'))

print('Go to the 6th byte in the file', f.seek(5))      # Go to the 6th byte in the file

print(f.read(1))
print('Go to the 3rd byte before the end', f.seek(-3, 2))  # Go to the 3rd byte before the end

print(f.read(1))



