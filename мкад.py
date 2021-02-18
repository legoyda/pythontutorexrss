#Universal pictures present
x = float(input())
magic = x // x
magic1 = magic * x
fin1 = float(x) - int(x)
fin2 = list(str(fin1))
if x == int(magic):
    print (fin2)
elif x != int(magic):
    print (fin2[2])