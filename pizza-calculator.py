#opdracht pizzacalulator
#Alwin Wezenbeek 99060433

pizzasmallprice = 5    #prijs van pizza small
pizzamediumprice = 7   #prijs van pizza medium
pizzalargeprice = 9    #prijs van pizza large

print('--------------------------------')
print('pizza small costs             5$')
print('pizza medium costs            7$')
print('pizza large costs             9$')
print('--------------------------------')

pizzasmall = int(input('hoeveel pizza small wil je? '))       #vraag 1
pizzamedium = int(input('hoeveel pizza medium wil je? '))     #vraag 2
pizzalarge = int(input('hoeveel pizza large wil je? '))       #vraag 3

totalsmall = (pizzasmallprice * pizzasmall)              #berekent de pizzasmal prijs maal de input van de gebruiker
totalmedium = (pizzamediumprice * pizzamedium)           #berekent de pizzamedium prijs maal de input van de gebruiker
totallarge = (pizzalargeprice * pizzalarge)              #berekent de pizzalarge prijs maal de input van de gebruiker

print ('dat is dan' ' ' + str(totalsmall + totalmedium + totallarge) + ' ''dollar') #totaal bedrag als eindbericht
