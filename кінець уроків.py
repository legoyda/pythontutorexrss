n = int(input())
m = int(input())
result = m //n
#print (result)
if result * n == m:
    print (result)
elif n%m >=1:
    print (result +1)
elif m < n:
    print ('1')