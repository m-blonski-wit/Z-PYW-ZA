# Funkcje nie sprawdzają czy na liście lstLista znajdują się liczby, ale jest to sprawdzane przy wypełnianiu list ocenami.
# Dla uproszczenia nie jest sprawdzana liczba ocen z danego przedmiotu. W przypadku niepodania ocen występuje błąd dzielenia przez zero.
# Założyłem, że częścią zadania jest samodzielne policzenie agregacji, zatem nie użyłem biblioteki statystycznej.
import statistics

def fltSrednia(lstLista):
    return sum(lstLista)/len(lstLista)

def fltMediana(lstLista):
    intPolowa,intReszta=divmod(len(lstLista),2)             # intReszta 0 lub 1, traktowana dalej jak zmienna logiczna
    if intReszta:
        return sorted(lstLista)[intPolowa]                  # dla nieparzystej liczby ocen
    return sum(sorted(lstLista)[intPolowa-1:intPolowa+1])/2 # dla parzystej liczby ocen średnia dwóch środkowych elementów lstLista

def fltOdchylenieStdPopul(lstLista):
    fltSredniaTmp=fltSrednia(lstLista)
    import math
    # dla każdej oceny w lstLista kwadrat odchylenia od średniej, suma elementów takiej listy podzielona przez liczbę ocen
    return math.sqrt(sum([(fltSredniaTmp-intOcena)**2 for intOcena in lstLista])/len(lstLista))

dctPrzedmOceny={}
print('Proszę podać przedmiot, a następnie oceny z zakresu 2-5.\nPusta wartość kończy wprowadzanie ocen/przedmiotów.')
while True:
    strPrzedmiot=input('Przedmiot: ')
    if strPrzedmiot=='':
        print('Wyniki')
        for strPrzedmiot in dctPrzedmOceny:
            print('Przedmiot: {0}, oceny: {1}, ocena średnia: {2:1.2f}, mediana ocen: {3:1.2f}, odchylenie standardowe ocen: {4:1.2f}.'.format(\
                strPrzedmiot,\
                    str(dctPrzedmOceny[strPrzedmiot])[1:-1]\
                        ,fltSrednia(dctPrzedmOceny[strPrzedmiot])\
                        ,fltMediana(dctPrzedmOceny[strPrzedmiot])\
                        ,fltOdchylenieStdPopul(dctPrzedmOceny[strPrzedmiot])\
                    ))
        break
    if strPrzedmiot in dctPrzedmOceny:
        print('Przedmiot {} już jest w słowniku.'.format(strPrzedmiot))
    else:
        dctPrzedmOceny[strPrzedmiot]=list()
        print('Przedmiot {} dodany do słownika.'.format(strPrzedmiot))
    while True:
        strOcena=input('Ocena: ')
        if strOcena=='':
            if len(dctPrzedmOceny[strPrzedmiot])<2:
                print("Zbyt mało ocen z przedmiotu {}. Podaj choć dwie.".format(strPrzedmiot))
                continue
            print('Koniec ocen z {}.'.format(strPrzedmiot))
            break
        try:
            intOcena=int(strOcena)
        except ValueError:
            print('Podana ocena: {} nie jest liczbą.'.format(strOcena))
        else:
            if 2<=intOcena<=5:
                dctPrzedmOceny[strPrzedmiot].append(intOcena)
            else:
                print('Podana ocena {} jest poza zakresem 2-5.'.format(strOcena))