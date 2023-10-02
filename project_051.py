n=int(input('enter the row number:'))
for i in range(n):
    print((str(i+1)+' ')*(i+1))
for i in range(n-1):
    print((str(n-i-1)+' ')*(n-i-1))
