x1 = int(input('>>'))
y1 = int(input('>>'))
x2 = int(input('>>'))
y2 = int(input('>>'))


a = 'black' if (x1+y1)%2 == 0 else 'White'
b = 'black' if (x1+y1)%2 == 0 else 'White'

if a == b:
    print ('YES')
else:
    print('NO')