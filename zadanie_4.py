import sys
intLiczbaLiczb=5
strLiczby=[]
intLiczby=[]
boolBlad=False

strLiczby=input('Proszę podać {} liczb całkowitych, oddzielając je przecinkiem: '.format(intLiczbaLiczb)).split(',')
if len(strLiczby)!=intLiczbaLiczb: 
    print('Błędna liczba liczb: {} zamiast {}.'.format(len(strLiczby),intLiczbaLiczb))
    boolBlad=True
else:
    for strTymczas in strLiczby:
        try:
            intTymczas=int(strTymczas)
        except:
            print ('{} nie jest liczbą całkowitą.'.format(strTymczas))
            boolBlad=True
        else:
            intLiczby.append(intTymczas)
if boolBlad==True:
    sys.exit('Niepoprawna lista liczb.')
else:
    print('Elementy listy liczb: {}.'.format(str(intLiczby)[1:-1]))

print('Elementy listy z indeksami:')
print('Indeks\t Liczba')
for intIndeks in range(len(intLiczby)):
    print('{}\t {}'.format(intIndeks,intLiczby[intIndeks]))

print('Elementy listy w odwrotnej kolejności, z indeksami:')
print('Indeks\t Liczba')
for intIndeks in range(len(intLiczby)-1,-1,-1):
    print('{}\t {}'.format(intIndeks,intLiczby[intIndeks]))

intLiczbySort=intLiczby.copy()
intLiczbySort.sort()

print('Lista posortowana: {}.'.format(intLiczbySort))

strTymczas=input('Proszę podać jedną z liczb z listy {}, zostanie z niej usunięta: '.format(str(intLiczby)))
try:
    intTymczas=int(strTymczas)
except:
    print('{} nie jest liczbą całkowitą.'.format(strTymczas))
    boolBlad=True
else:
    if not intTymczas in intLiczby:
        print('{} nie znajduje się wśród elementów listy {}.'.format(intTymczas,str(intLiczby)))
        boolBlad=True
if boolBlad:
    exit()

intLiczbyTemp=intLiczby.copy()
intLiczbyTemp.remove(intTymczas)

print('Lista z usuniętym pierwszym wystąpieniem {}: {}.'.format(intTymczas,intLiczbyTemp))

strTymczas=input('Proszę podać indeks jednej z liczb z listy {}, liczba o tym indeksie zostanie usunięta: '.format(str(intLiczby)))
try:
    intTymczas=int(strTymczas)
except:
    print('{} nie jest liczbą całkowitą.'.format(strTymczas))
    boolBlad=True
else:
    if not(0<=intTymczas<len(intLiczby)):
        print('{} spoza zakresu indeksów listy {}.'.format(intTymczas,str(intLiczby)))
        boolBlad=True
if boolBlad:
    exit()

intLiczbyTemp=intLiczby.copy()
intLiczbyTemp.pop(intTymczas)

print('Lista z usuniętym elementem o indeksie {}: {}.'.format(intTymczas,intLiczbyTemp))

