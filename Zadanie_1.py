try:
    a,b,c=input("Proszę podać trzy liczby, oddzielając je przecinkiem: ").split(',')
except:
    print('Podano nieprawidłowe dane.')
else:
    print("Pierwsza liczba:{}, druga liczba:{}, trzecia liczba:{}.".format(a,b,c))
    m=min(a,b,c)
    print("Najmniejsza liczba z {}, {}, {} to {}.".format(a,b,c,m))