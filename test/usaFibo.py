#! python

#TEMA __MAIN__
#CUANDO HAGO if __name__=='__main__'
#Lo que hago es preguntar si el nombre del modulo es __main__. Esto ocurre cuando el modulo es el llamado desde el shell.
#Todos los modulos llamados desde el shell son __main__

import os #ESTO SI IMPORTA LOS NOMBRES DEL MODULO

from fibo import fib # ESTO NO IMPORTA LOS NOMBRES DEL MODULO y puedo llamar a fib sin hacer fibo.fin()

#SI hago from fibo import *, importo todos los nombres excepto los que comienzan con __
#SE RECOMIENDA NO USAR * en script, solo cuando estoy en modo comando.

os.system('cls')

#print ("Nombre del módulo: ",fibo.__name__) #NO FUNCIONA PORQUE IMPORTE CON FROM
print(os.__name__)
n=int(input("Ingrese el número:"))

fibonacci=fib(n) # si hubiera hecho import fibo, entonces sería fibo.fib(n)
print ("Serie de Fibonacci:",end=' ')
for f in fibonacci:
    print (f,end=' ')
