import math
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))


def calcDesc(a, b, c):
    return b ** 2 - 4 * a * c


def calcX(a, b, desccr):
    if desccr > 0:
        x1 = ((-b) + math.sqrt(descr)) / 2 * a
        x2 = ((-b) - math.sqrt(descr)) / 2 * a
        return ["x1 = " + str(x1), "x2 = " + str(x2), "D = " + str(desccr)]
    elif desccr == 0:
        x1 = ((-b) + math.sqrt(descr)) / 2 * a
        return ["x1 = " + str(x1), "D = " + str(desccr)]
    else:
        return ['NO']


descr = calcDesc(a, b, c)

result = calcX(a, b, descr)

for r in result:
    print(r)