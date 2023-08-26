print("------------------a--------------")

edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
edades.sort()
print("El orden correcto vendria ser: ",edades)
edad_Min = min(edades)
edad_Max = max(edades)

print("------------------b--------------")

edades.insert(0, edad_Min)
edades.insert(0, edad_Max) 

print("Las edades se incluyen al inicio: ",edades)

print("------------------c--------------")

edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
termino_Medio = (edades[4],  edades[5])
primer_ele, segundo_ele = termino_Medio
resultado = (primer_ele + segundo_ele)/2

print("La edada mediana es: ",resultado)

print("------------------d--------------")

edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
suma = sum(edades)
lista = len(edades)
promedio = (suma / lista)
print("El promedio es: ",promedio)

print("------------------e--------------")

edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
num_Max = max(edades)
num_Min = min(edades)
rango = (num_Max - num_Min)
print("El rango es:",rango)

print("------------------f--------------")

edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
valor_Min = min(edades)
valor_Max = max(edades)
promedio = (sum(edades) / len(edades))
result_1 = (valor_Min - promedio), abs(valor_Min - promedio)
result_2 = (valor_Max - promedio), abs(valor_Max - promedio) 

print(result_1)
print(result_2)

print(diferencia_minima = abs(valor_Min - promedio))
print(diferencia_maxima = abs(valor_Max - promedio))