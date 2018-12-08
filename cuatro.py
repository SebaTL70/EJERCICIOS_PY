lista=[1,2,3,4,5,6,7,8,9,0]
#imprimo lista
print("TODA LA LISTA:",end='\t---->')
print(lista)
print("LISTA 1 X 1:")
#imprimo lista 1 x 1
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])
print(lista[5])
print(lista[6])
print(lista[7])
print(lista[9])

#para cada elemento de la lista saco su cuadrado
print("El cuadrado de cada elemento de la lista:")
for x in lista:
    print(x,":",x**2)

lista.append(200)

print(lista,"....agregue el 200 con append()")

lista.extend(range(500,510))

print(lista,"...extendi la lista con los numero del 500 a 509-son 10-con extend()")

lista.insert(10,'HOLA')

print(lista,"... en la posicion 10 inserte hola con insert(index,elemento)")

lista.remove(0)

print(lista,"....Elimine el primer elemento que sea 0 con REMOVE(0)")


lista.clear()

print(lista,"...limpie la lista con clear()...esto equivale a del lista[:]")

lista=[10,20,30,40,50,60,70,80,90]

print(lista,"..NUEVA LISTA")

lista.reverse()

print(lista,"....invierto la lista con REVERSE()")

listaB=lista

print(listaB,"listaB=lista")

listaB=lista[:]

print(listaB,"...listaB=lista[:]")

listaB=lista.copy()

print(listaB,"...y esto es listaB=lista.copy()")
listaB.reverse();listaB.append(299)
print(listaB,"...se hizo un reverser()  a la lista y un append(299) pero las 2 instrucciones en una linea separadas por ;")

del listaB[:]

print(listaB,"..elimine la listaB con del listaB[:]")


lista.append(12345)
print(lista)