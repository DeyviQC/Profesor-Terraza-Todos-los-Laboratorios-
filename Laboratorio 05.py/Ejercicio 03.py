print("--------------------------------")

# Listas de números enteros
lista1 = (1,2,3,4,5,6,7,8,9,10)
lista2 = (5,6,7,8,9,10,11,12,13,14,15)
lista3 = (10,11,12,13,14,15,16,17,18,19,20)

print("------------------a--------------")

#Convierte las listas en conjuntos
conjunto1 = set(lista1)
conjunto2 = set(lista2)
conjunto3 = set(lista3)
print(conjunto1)
print(conjunto2)
print(conjunto3)

print("------------------b--------------")

#Encuentra el conjunto de todos los números que están presentes en las tres listas
conjunto_comun = conjunto1 & conjunto2 & conjunto3
print("Conjunto de números en común:", conjunto_comun)

print("------------------c--------------")

#Encuentra el conjunto de todos los números que están presentes en al menos una de las listas
conjunto_union = lista1 + lista2 + lista3
union=set(conjunto_union)
print("Conjunto de números en al menos una lista:", union)

print("------------------d--------------")

#Encuentra el conjunto de todos los números que están presentes en la primera lista, pero no en la última
conjunto_diferencia = conjunto1 - conjunto3
print("Conjunto de números en la primera lista pero no en la última:", conjunto_diferencia)

print("------------------e--------------")

#Convierte los conjuntos obtenidos en tuplas y suma el primer y último elemento de cada tupla
tupla_comun = (list(conjunto_comun)[0], list(conjunto_comun)[-1])
Suma1=sum(tupla_comun)
tupla_union = (list(conjunto_union)[0], list(conjunto_union)[-1])
Suma2=sum(tupla_union)
tupla_diferencia = (list(conjunto_diferencia)[0], list(conjunto_diferencia)[-1])
Suma3=sum(tupla_diferencia)

print("Tupla de suma de primer y último elemento en conjunto de común:", Suma1)
print("Tupla de suma de primer y último elemento en conjunto de unión:", Suma2)
print("Tupla de suma de primer y último elemento en conjunto de diferencia:", Suma3)
