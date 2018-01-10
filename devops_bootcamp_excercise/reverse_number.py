while True:
    try:
        num = int(input("Enter any number\n"))
        break;
    except ValueError:
        print("Oops ! that's not a valid integer")
    except Exception as ex:
        print(ex)

reverse_number = 0
tmp_num = num
while(num > 0):
    reminder = num%10
    reverse_number = (reverse_number*10) + reminder
    num = int(num/10)
    #print(reverse_number, "--", reminder, "--", num, "\n")

print("Reversed number is ",reverse_number)
print("Reversed number is ",tmp_num.__str__()[::-1])
print("Reversed number is ",str(tmp_num)[::-1])
