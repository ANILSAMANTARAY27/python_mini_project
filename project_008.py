n=int(input('enter the row number:'))
for i in range(n):
    for j in range(n):
        print(chr(65+j),end=' ')
    print()