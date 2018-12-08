#listas como pilas

from collections import deque


cola=deque([1,2,3,4,5]) #deque es cola


print("una cola ",cola)

cola.append("terry")

print("llega terry ",cola)

cola.popleft()

print("El 1 que llego primero sale ",cola)


pila=[1,2,3,4,5,6]

pila.append(200)

print(pila)

pila.pop()
print(pila)




