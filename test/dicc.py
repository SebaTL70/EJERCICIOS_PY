#! python

print("\n#DICCIONARIOS ANIDADOS")

persona={
    'nombre':{
        "primero":"Juan",
        "segundo":"Francis"
    },
    'apellido':{
        "primero":"Gonzalez",
        "segundo":"Rodriguez"
    }
}

for campo,contenido in persona.items():
    print("\n*",campo,end=":")
    for primero,segundo in contenido.items():
        print(segundo,end=" ")

biblioteca={
    'seccion':{
        'uno':{
            'exactas':{
                'matematica':{
                    'calculo':{
                        'titulo':'Caluclo Facial',
                        'auto':'yo mismo',
                        'edicion':1993
                    },
                    'aritmetica':{
                     'titulo':'la directriz',
                     'autor':'aquel',
                     'edicion':1233
                    }
                }
            }
        }
    }
   # 'departamento':'unico'
    
}
print("\n")
for seccion,contenido in biblioteca.items():
    print("El item de la biblioteca se llama: {}".format(seccion))
    
    for numero,ciencia in contenido.items():
        print("La unidad es:{}".format(numero))

        for nombre, disciplina in ciencia.items():
            print("La ciencia es:{}".format(nombre))

            for nombre,campo in disciplina.items():
                print("La disciplina es : {}".format(nombre))

                for nombre,libro in campo.items():
                    print("El campo es:{}".format(nombre))
                    print("\nLibro:")
                    for elemento,detalle in libro.items():
                        
                        print("{:>20}:{}".format(elemento.title(),detalle)) 
        
               
