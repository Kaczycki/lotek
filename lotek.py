""" totolotek - symulacja"""
import random
WYNIKI_LOSOWANIA = set() #wylosowane liczby
skreslone = set() #skreslone liczby
trafione = set()
three = 0
four = 0
five = 0
zakres = 20
LICZBA_LOSOWAN = 0
CENA=3

def losuj():
    """_summary_:losuje 6 niepowtarzalnych liczb od 1 do 49

    Returns:
        _type_:set -> WYNIKI_LOSOWANIA
    """
    WYNIKI_LOSOWANIA=set()
    while len(WYNIKI_LOSOWANIA) != 6:
        #los = random.randrange(1, zakres)
        #WYNIKI_LOSOWANIA.add(los)
        WYNIKI_LOSOWANIA = random.sample(range(1,zakres), 6)
    return WYNIKI_LOSOWANIA

if __name__ == '__main__':
    while len(skreslone) != 6: #pyta o 6 niepowtarzalnych liczb 1 do 49
        current_input = int(input('skreśl swoją liczbę '))
        if current_input and current_input > 0 and current_input < zakres:#not in skreslone 
            skreslone.add(current_input)
    print (f'wytypowane liczby, to {skreslone}')
    trafione = WYNIKI_LOSOWANIA.intersection(skreslone)

    while len(trafione) < 6: 
        """ szuka sześciu wspólnych liczb
            (skreślonych i wylosowanych)"""
        trafione = set(losuj()).intersection(skreslone)
        LICZBA_LOSOWAN += 1
        if len(trafione) == 5:
            five += 1
        elif len(trafione) == 4:
            four =+ 1
        elif len(trafione) == 3:
            three =+ 1


print('______')
print('wygrana!')
print(WYNIKI_LOSOWANIA)
print(f'trafiona szóstka za {LICZBA_LOSOWAN} losowaniem')
print(f'losowania w środy i soboty przyniosły wygraną po {LICZBA_LOSOWAN/2/52} latach')
print(f'po drodze trafiło się {five} piątek, {four} czwórek, {three} trójek')
#Trafienie 6 z 49 liczb oznacza wygraną 1 000 000 zł.
# #„Piątka” to 3500 zł, „czwórka” – 100 zł, a „trójka” – 10 zł.
prize = 1000000 + 3500 * five + 100 * four + 10 * three
print(f'Łączna wygrana: {prize} złotych')
print(f'wydane {CENA*LICZBA_LOSOWAN} złotych, przy cenie {CENA} za los. Warto było?')