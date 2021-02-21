n=int(input('Quanti elementi?:'))
lista=[n]

for i in lista:
    numero=String(input('Elemento:'))
    lista.insert(0,numero)

c=0
for i in range(n):
    print('Elemento in posizione:', i, 'vale', lista[i])
    if lista[i]>=50 and lista[i]<=100:
        c+=1

print('Ci sono in tutto', c ,'elementi compresi nell\'intervallo')

