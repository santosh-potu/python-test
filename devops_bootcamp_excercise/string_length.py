str = ''
length = 0
while (length < 1):
    str = input("Enter any valid string\n")
    length = str.replace(" ","").__len__()
    if length == 0:
        print("Entered String length is zero\n")

print("Length of '",str,"' is (excluding spaces):",length)