from os import remove
from random import randint
import sys
intWielkoscPuli=49      # liczba liczb z których losujemy
intWielkoscZakladu=6    # liczba losowanych liczb
#intWielkoscZakladu=6    # liczba obstawianych liczb
intPula=[]
intLosowanie=set()
strZaklad=[]
intZaklad=set()
boolBlad=False

strZaklad=input('Proszę podać {} liczb z zakresu 1-{}, oddzielając je przecinkiem: '.format(intWielkoscZakladu,intWielkoscPuli)).split(',')
if len(strZaklad)!=intWielkoscZakladu: 
    print('Błędna liczba pozycji zakładu: {} zamiast {}.'.format(len(strZaklad),intWielkoscZakladu))
    boolBlad=True
else:
    for strTymczas in strZaklad:
        try:
            intTymczas=int(strTymczas)
        except:
            print ('{} nie jest liczbą całkowitą.'.format(strTymczas))
            boolBlad=True
        else:
            if 1<=intTymczas<=intWielkoscPuli:
#                print ('{} OK'.format(intTymczas))
                if intTymczas in intZaklad:
                    print('{} obstawiono przynajmniej dwukrotnie.'.format(intTymczas))
                    boolBlad=True
                else:
                    intZaklad.add(intTymczas)
            else:
                print('{} jest poza zakresem'.format(strTymczas))
                boolBlad=True
if boolBlad==True:
    sys.exit('Zakład niepoprawny.')
else:
    print('Zakład: {}.'.format(str(intZaklad)[1:-1]))

for intTymczas in range(intWielkoscPuli):
    intPula.append(intTymczas+1)

print('Losowanie')
for intTymczas in range(intWielkoscZakladu):
    intLosowanie.add(intPula.pop(randint(1,len(intPula))))

for intTymczas in intLosowanie:
    try:
         intZaklad.remove(intTymczas)
         print('{} - trafienie.'.format(intTymczas))
    except:
        print('{} - pudło.'.format(intTymczas))

print('Wynik losowania: {}.'.format(str(intLosowanie)[1:-1]))
print('Liczba trafień: {}.'.format(intWielkoscZakladu-len(intZaklad)))