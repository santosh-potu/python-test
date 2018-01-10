
def print_dashes(num_of_dashes =4):

    for i in range(2):
        print("+", end='')
        for i in range(num_of_dashes):
            print(" - ",end='')
    print('+')

def print_lines(num_of_lines=4,num_of_dashes=4):
    for i in range(num_of_lines):
        print('|','  '*num_of_dashes,'  |','  '*num_of_dashes,'  |')


print_dashes()
print_lines()
print_dashes()
print_lines()
print_dashes()
