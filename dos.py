cadena="HOLA MUNDO"
print(cadena)

print(cadena[0])

print(cadena[5:])

print(cadena[:-2])

for x in cadena:
    print(x)

cadena2="cadena1" "cadena2" "cadena3"

print(cadena2)

for x in range(0,len(cadena)):
    print(cadena[x])

list1=[1,2,3,4,5,6,7,8,9,0]

for x in list1:
    print(str(x)+" "+str(x**2))

#concatenacion de listas
lista=list1+[11,12,13,14,15,"hola"]

for x in lista:
    print(x)

#slice de listas

lista3=lista[-6:-1]

print(lista3)

print(lista[3:5])

#vaciar un slice con lista vacia
print(lista)
lista[-3:-1]=[]
print(lista)

#listas anidadas
list1=[1,2,3,4]
list2=[5,6,7,8]

lista=[list1,list2]

print(lista)
print(list1)
print(list2)


a,b=0,1
while b<10:
    print(b,end=" - ")  #el parametro end='xxxx' cambia el salto de linea por default por otro
    a,b=b,a+b
    