#! python

import sys

print("\n#USO ITEMS() para obtener el par clave-valor.")
yo={"nombre":"Sebastián","apellido":"Levi","edad":46}
for campo,valor in yo.items():
    print (campo,"->",valor)

print("\n#USO ENUMERATE(lista) PARA OBTENER el par indice-valor")
secuencia=['uno','dos','tres']
for indice,valor in enumerate(secuencia):
    print(indice,":",valor)

print("\n#USO ZIP para RECORRER 2 listas en paralelo.")
nombre=["Juan","Pedro","Gustavo"]
puesto=["Director","Peón","Portero"]
for n,p in zip(nombre,puesto):
    print("El cargo de {0} es {1}".format(n,p))

print("\n#ITERO UNA LISTA EN ORDEN INVERSO CON REVERSE()")
for i in reversed(range(1,10,2)):
    print(i,end=',')
print("FIN.")


biblioteca={
    "libro":"Viaje al centro",
    "autor":"Julio VErne",
    "edicion":1895
}
print("\nLibreria")
for campo, contenido in biblioteca.items():
    print ("Libro {0} : {1}".format(campo,contenido))

sys.stdout.write("\nHOLA MUNDO\nVersion: %s" % (sys.version))


listaX=['juan','pedro','mario','luis']

for ind,cont in enumerate(listaX):
    print("EL indice es {} y el contenido es {}.".format(ind,cont))

for ind,cont in enumerate(listaX):
    print(ind,":",cont)


print ("El texto dice :{:_>10}".format('HOLA'))


print ("El texto dice :{:#>20}".format('HOLA'))


print("\n---------------------------ITEMS()")
fichaJuan={
    "nombre":"JUAN",
    "apellido":"GONZALEZ",
    "edad":46
}
for clave,contenido in fichaJuan.items():
    print(clave,":",contenido)


print("\n---------------------------ENUMERATE()")
verduras=['lechuga','remolacha','verdeo']
for indice,verdura in enumerate(verduras):
    print("Verdura {}: {}".format(indice,verdura))


print("\n---------------------------ZIP()")

puesto=['PRIMERO','SEGUNDO','TERCERO']
nombre=['SANTI','JOSE','PEDRO',"juan"]

for p,n in zip(puesto,nombre):
    print("El puesto {} es para {}.".format(p,n))


print("\n---------------------------REVERSED()")
for x in reversed(range(1,10,2)):
    print(x)


print("\n---------------------------ZIP/REVERSED")
for p,n in zip(puesto,reversed(nombre)):
    print("El puesto {} es para {}.".format(p,n))