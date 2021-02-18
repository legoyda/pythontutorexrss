a = int(input())  # відстань між рядами
b = int(input())  # відстань між дирочками в ряду
l = int(input())  # довжина вільного кінця шнурка
N = int(input())  # кількість дирочок в кожному ряду

goriz = a*(N-1)
vertik = b*(N-1)
l1 = ((l*2)+(goriz*2)+(vertik*2))
print (l1 + a)