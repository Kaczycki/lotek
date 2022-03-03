""" totolotek - symulacja"""
import random
#print (random.random()*100)
wyniki_losowania = set() #wylosowane liczby
skreslone = set() #skreslone liczby
trafione = set()

while len(wyniki_losowania) != 6: #losuje 6 niepowtarzalnych liczb od 1 do 49
    los = random.randrange(1, 50)
    if los not in wyniki_losowania:
        wyniki_losowania.add(los)
    print (wyniki_losowania)

while len(skreslone) != 6: #pyta o 6 niepowtarzalnych liczb 1 do 49
    current_input = input("skreśl swoją liczbę")
    if current_input not in skreslone:
        skreslone.add(current_input)
    print (skreslone)

trafione = wyniki_losowania.intersection(skreslone)



while len(trafione) == 0: #szuka wspólnych liczb (skreślonych i wylosowanych)
  while len(wyniki_losowania) != 6: #losuje 6 niepowtarzalnych liczb od 1 do 49
    los = random.randrange(1, 50)
    if los not in wyniki_losowania:
        wyniki_losowania.add(los)
    print (wyniki_losowania)
  trafione = wyniki_losowania.intersection(skreslone)


print("wygrana!")
print(wyniki_losowania)
print(trafione)

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