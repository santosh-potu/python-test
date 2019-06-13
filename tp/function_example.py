def printinfo(name,age=35):
    "This prints passed info to a function"
    print("name",name)
    print("age",age)
    return

def print_varible_length(arg1, *vartuple):
    "This function prints variable lenth parameters"
    print(arg1)
    for item in vartuple:
        print(item)
    return

sum = lambda arg1,arg2: arg1+arg2;

printinfo(age=45,name="someX")
printinfo(name="someY")

print_varible_length(20)
print_varible_length(30,40,50,60)

print(sum(10,90))
