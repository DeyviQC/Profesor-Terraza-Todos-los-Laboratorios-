mensaje = input("Ingrese el mensaje: ")
desplazamiento = int(input("Ingrese el numero de desplazamiento: "))

alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfabeto1='abcdefghijklmnopqrstuvwxyz'
mensajenuevo =" "

for caracter in mensaje:
    if caracter in alfabeto:  
        indice = alfabeto.index(caracter)
        nuevo_indice = (indice + desplazamiento)%26
        mensajenuevo += alfabeto[nuevo_indice]

    elif caracter in alfabeto1:
        indice = alfabeto1.index(caracter)
        nuevo_indice = (indice + desplazamiento)%26
        mensajenuevo += alfabeto1[nuevo_indice]

print("Mensaje cifrado:", mensajenuevo)
