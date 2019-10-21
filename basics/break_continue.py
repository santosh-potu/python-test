for n in range(2,10):
    for x in range(2,n):
        if n%x == 0 :
            print(n, 'equals', x, '*', n // x)
            break
        else:
            print (n," is a prime number")

for n in range(2,10):
    if n % 2 == 0 :
        print ("Found Even number ",n)
        continue
    print(" odd number",n)