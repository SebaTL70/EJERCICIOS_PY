juan=['juan','garcia',24,5000,'pintor']
maria=['maria','lopez',20,6000,'secretraria']

pedro=['pedro','lopez',20,6000,'secretraria']

print (juan)

personas=[juan,maria]

print(personas[1])


personas.append(pedro)
print(20*'-')
for x in personas:
    print(x)

personas[len(personas):]=range(1,10) ######agrega desde el final de la lista un iterable
personas.extend(range(11,20))#####hace lo mismo

for x in personas:
    print(x)

personas.insert(1,"LOCO")###INSERTA DESPLAZANDO EL QUE SIGUE
###insert(len(personas),"LOCO") es lo mismo que personas.append("loco")
for x in personas:
    print(personas.index(x),":",x)

personas.remove("LOCO")

for x in personas:
    print(personas.index(x),"--",x)

#personas.remove("cacac")####DA ERROR PORQUE NO EXISTE

personas.pop(20)# ELIMINA EL INDEX 20

for x in personas:
    print(personas.index(x),">>>>",x)

#personas.clear()# ELIMINA TODOS LOS ELEMENTOS DE  LA LISTA
#del personas [:] #HACE LO MISMO

#print(personas)# VACIO

posicion=personas.index(juan)

print("La posición de juan es",posicion)

#posicion=personas.index(maria,3)#NO LO ENCUENTRA PORQUE EMPIEZA A BUSCAR DESDE LA POS:3
posicion=personas.index(maria,0,4)#LO BUSCA ENTRE 0 y 4=> lo ENCUENTRA
print("La posicion de Maria ",posicion)

ocurrencias_de_x=personas.count(11)

print(ocurrencias_de_x)

personas.insert(4,11)# INSERTO en pos 4 a el 11

ocurrencias_de_x_ahora=personas.count(11)# ahora son 2 veces

print(ocurrencias_de_x_ahora)

print("la primera ocurrencia del 11 es en la pos ",personas.index(11))

vocales=['o','i','a','u','e'] #lista desordenada

vocales.sort()#ordena la lista ---ver KEY=..... y REVERSE=..... son los parametros, se puede usar SORTED(lista,key,reverse)

print(vocales)

vocales.reverse()#invierte los elementos
print(vocales)

lista=[1,2,3,4,5,6,7,8,9,0]

for x in lista:
    cuadrado=x**2
    if cuadrado%2 ==0:
        print(cuadrado, " es cuadrado")
        continue
    print (cuadrado)






def tabla(numero=4):
    for x in range(1,11):
        print(numero,"*",x,"=",str(int(numero)*x))

numero=input("INGRESE UN NUMERO:")
tabla(numero) # si llamo tabla(), asume que el número es 4(valor por omision)

respuesta=input("GUSTO? ")
if respuesta in ('s','S'):
    print("siiiii")
else:
    print("no")

print (eval(input("concatena ej : 'hola'+' '+'muno' o x ej: 2*3:")))

print(list(range(1,11))) #PRINT ,LIST(), RANGE(), LIST crea una lista a partir de un iterable (range)
