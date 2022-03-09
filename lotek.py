""" totolotek - symulacja"""
import random
wyniki_losowania = set() #wylosowane liczby
skreslone = set() #skreslone liczby
trafione = set()
LICZBA_LOSOWAN = 0
CENA=3
def wylosuj_6 ():
    """_summary_
    losuje 6 niepowtarzalnych liczb od 1 do 49

    Returns:
        set: random 6 numbers range 1-49
    """
    while len(wyniki_losowania) != 6: 
        los = random.randrange(1, 50)
        wyniki_losowania.add(los)
    return wyniki_losowania
    

while len(skreslone) != 6: #pyta o 6 niepowtarzalnych liczb 1 do 49
    current_input = int(input('skreśl swoją liczbę '))
    if current_input and current_input > 0 and current_input < 50:#not in skreslone 
        skreslone.add(current_input)
print (f'wytypowane liczby, to {skreslone}')

trafione = wyniki_losowania.intersection(skreslone)

while len(trafione) < 6: #szuka wspólnych liczb (skreślonych i wylosowanych)
    wyniki_losowania=set()
    while len(wyniki_losowania) != 6: #losuje 6 niepowtarzalnych liczb od 1 do 49
        los = random.randrange(1, 50)
        if los not in wyniki_losowania:
            wyniki_losowania.add(los)
    trafione = wyniki_losowania.intersection(skreslone)
    #print(wyniki_losowania)
    #print ('trafione: ', trafione)
    LICZBA_LOSOWAN += 1
    #if LICZBA_LOSOWAN%10000 == 0:
    #    print (LICZBA_LOSOWAN)

print('______')
print('wygrana!')
print(wyniki_losowania)
print(f'trafione za {LICZBA_LOSOWAN} losowaniem')
print(f'wydane {CENA*LICZBA_LOSOWAN} złotych, przy cenie {CENA} za los. Warto było?')
print(f'losowania w środy i soboty przyniosły wygraną po {LICZBA_LOSOWAN/2/52} latach')
