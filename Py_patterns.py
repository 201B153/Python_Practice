'''Here the code's are starting from # and there specifications are given with '''

## patterns
n = int(input('Enter the no. of rows u want to print \n'))
# triangle
for row in range(1,n+1):
    for column in range(1,row+1):
        print('*',end = ' ')
    print()
# reverse triangle
for row in range(n,0,-1):
    for column in range(1, row+1):
        print('*', end = " ")
    print()
# two join triangles
for row in range(1,n+1):
    for column in range(1,row+1):
        print('*',end = ' ')
    print()
for row in range(n-1,0,-1):
    for column in range(1, row+1):
        print('*', end = " ")
    print()
# for numerical patterns
for row in range(1,n+1):
    for column in range(1,row+1):
        print(column,end = ' ')
        column = column+1
    print()
#for nulti digit values
for row in range(1,n+1):
    for column in range(1,row+1):
        print('{0}{1}'.format(row,column),end = ' ')
    print()
#alphabetic characters pattern
ch = 65
for row in range(1,n+1):
    for column in range(1,row+1):
        print('{0}'.format(chr(ch)),end = ' ')
        ch = ch+1
    print()
ch = ch-(n+1)
for row in range(n-1,0,-1):
    for column in range(1, row+1):
        print('{0}'.format(chr(ch)),end = ' ')
        ch = ch-1
    print()
# alphabetic order pattern
ch=64
for row in range(1,n+1):
    for column in range(1,row+1):
        print('{0}'.format(chr(ch+column)),end=' ')
    print()
for row in range(n-1,0,-1):
    for column in range(1,row+1):
        print('{0}'.format(chr(ch+column)),end=' ')
    print()
#countinous numerical digits
sum = 0
for row in range(1,n+1):
    for column in range(1,row + 1):
        sum = sum+1
        print('{:02d}'.format(sum), end=' ')
    print()
sum = sum-(n)
for row in range(n-1,0,-1):
    for column in range(1,row+1):
        print('{:02d}'.format(sum),end=' ')
        sum = sum - 1
    print()
# high level star programs
# i = row and J= column
for i in range(n):
    for j in range(i,n):
        print(' ',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()
# decreeasing patterns
for i in range(n):
    for j in range(i):
        print(' ',end=' ')
    for j in range(i,n):
        print('*',end=' ')
    print()
# hill patterns
for i in range(n):
    for j in range(i,n):
        print(' ',end=' ')
    for j in range(i):
        print('*',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()
# hills reverse
for i in range(n):
    for j in range(i+1):
        print(' ',end=' ')
    for j in range(i,n-1):
        print('*',end=' ')
    for j in range(i,n):
        print('*',end=' ')
    print()
#diamond pattern
for i in range(n):
    for j in range(i,n):
        print(' ',end=' ')
    for j in range(i):
        print('*',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()
for i in range(n):
    for j in range(i+1):
        print(' ',end=' ')
    for j in range(i,n-1):
        print('*',end=' ')
    for j in range(i,n):
        print('*',end=' ')
    print()
#embidient patterns
for i in range(6):
    for j in range(7):
        if (i==0 and j%3!=0) or (i==1 and j%3==0) or (i-j==2) or (i+j==8):
            print('*',end='')
        else:
            print(end=' ')
    print()
#alphabetic characters
for i in range(7):
    for j in range(5):
        if ((j==0 or j==4) and i!=0 ) or ((i==0 or i==3) and (j>0 and j<4)):
            print('*',end='')
        else:
            print(' ',end='')
    print()
#square of '+' and '-'
for i in range(6):
    for j in range(6):
       if(i==0 or i==5) and (j==0 or j==5):
           print('+',end=' ')
       elif(i==0 or i==5) and (j!=0 or j!=5):
           print('-', end=' ')
       elif (i != 0 or i != 5) and (j == 0 or j == 5):
           print('-', end=' ')
       else:
           print(' ',end=' ')
    print()
#matrix of above problem
for i in range(n+1):
    for j in range(n+1):
       if(i%5==0 or i/5==1) and (j%5==0 or j/5==1):
           print('+',end=' ')
       elif(i%5==0 or i/5==1) and (j/5!=1 or j%5!=0):
           print('-', end=' ')
       elif (i%5!= 0 or i/5 !=1) and (j%5 == 0 or j/5 == 1):
           print('-', end=' ')
       else:
           print(' ',end=' ')
    print()