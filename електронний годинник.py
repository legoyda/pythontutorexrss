zn = int(input())
hor = zn//60 # значення годин
min = zn-(zn//60*60)
if hor<=23:
    print (hor,' ',min)
elif zn:
    print ((((zn-(zn//60//24*24*60))//60)),min) # ВИВІД ГОДИН НЕЗАОЛЕЖНОСТІ ВІД КІЛЬКОСТІ СУТОК


