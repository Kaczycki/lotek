""" totolotek - symulacja"""
import random
#print (random.random()*100)
wyniki_losowania = set() #wylosowane liczby
skreslone = set() #skreslone liczby
trafione = set()
liczba_losowan = 0

def wylosuj_6 ():
    while len(wyniki_losowania) != 6: #losuje 6 niepowtarzalnych liczb od 1 do 49
        los = random.randrange(1, 10)
        if los not in wyniki_losowania:
            wyniki_losowania.add(los)
    return (wyniki_losowania)


while len(skreslone) != 6: #pyta o 6 niepowtarzalnych liczb 1 do 49
    current_input = int(input('skreśl swoją liczbę '))
    if current_input not in skreslone:
        skreslone.add(current_input)
    print (skreslone)

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
    liczba_losowan += 1
    #if liczba_losowan%10000 == 0:
    #    print (liczba_losowan)



print('______')
print('wygrana!')
print(wyniki_losowania)
print(trafione, ' za ',liczba_losowan, ' losowaniem')


""" input:
    6 liczb
    częstotliwość losowań
    cena losu"""

""" procedury:
    przyjmij dane
    losuj, dopóki wynik nie będzie równy danym wejściowym
        w pętli licz losowania
    policz cenę łączną
    wyświetl liczbę losowań, cenę, czas potrzebny na wygraną"""

""" dane:
    zbiór kolejnych 49 liczb
    liczby wytypowane
    cena losu
    częstotliwość losowań
    łączna cena
    łączna liczba losowań
    """