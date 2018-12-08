cadena="Hermoso"

print(cadena[0])

print(cadena[0:4])

for x in cadena:
    print(x)

w=input("Ingrese un número:")


lista=[]
for x in range(1,11):
    print (str(w)+" x "+str(x)+" = "+str(int(w)*x))
    lista.append(int(w)*x)

print("-----LISTA-----")

for x in lista:
    print(x)

diccionario={"nombre":"seba","apellido":"levi"}

print(diccionario["nombre"])
print(diccionario["apellido"])

diccionario['edad']=46

print(diccionario["edad"])

print(diccionario.get("color") is None) #va a imprimir true : seria asi: "la clave color no existe", da true

print(diccionario.get("nombre") is None) # va a da False xq' estoy diciento:" la clave nombre no existe".

#print("el path es c:\directorio1\su2\")