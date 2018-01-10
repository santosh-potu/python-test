
operator_list = ['-','+','*','/','%']
while True:
        ops = input("Enter operator('-','+','*','/','%') :")
        if(ops in operator_list):
            break


while True:
        num1 = input("Enter number1=")
        if(num1.isdigit()):
            break

while True:
        num2 = input("Enter number2=")
        if(num2.isdigit()):
            break

try:
    if ops.__eq__('-'):
        print(num1," ",ops,' ',num2,' = ',float(num1)-float(num2))
    elif ops.__eq__('+'):
        print(num1, " ", ops, ' ', num2, ' = ', float(num1)+float(num2))
    elif ops.__eq__('*'):
        print(num1, " ", ops, ' ', num2, ' = ', float(num1)*float(num2))
    elif ops.__eq__('/'):
        print(num1, " ", ops, ' ', num2, ' = ', float(num1)/float(num2))
    else:
        print(num1, " ", ops, ' ', num2, ' = ', float(num1)%float(num2))
except ZeroDivisionError:
    print("Division by Zero")
except Exception as e:
    print(e)
