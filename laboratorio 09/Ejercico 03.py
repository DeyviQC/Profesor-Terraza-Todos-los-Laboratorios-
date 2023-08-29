import string
import random

def generar_contraseña(longitud, incluir_mayusculas=True, incluir_minusculas=True, incluir_numeros=True, incluir_especiales=True):
    caracteres = ""
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_especiales:
        caracteres += string.punctuation
    
    if caracteres == "":
        raise ValueError("Debes incluir al menos un tipo de carácter.")
    
    contraseña_generada = ''.join(map(lambda _: random.choice(caracteres), range(longitud)))
    return contraseña_generada


try:
    longitud = int(input("Ingrese la longitud de la contraseña: "))
    mayusculas = input("Incluir letras mayúsculas (S/N): ").upper() == "S"
    minusculas = input("Incluir letras minúsculas (S/N): ").upper() == "S"
    numeros = input("Incluir números (S/N): ").upper() == "S"
    especiales = input("Incluir caracteres especiales (S/N): ").upper() == "S"

    contraseña_generada = generar_contraseña(longitud, mayusculas, minusculas, numeros, especiales)
    print("Contraseña generada:", contraseña_generada)
except ValueError as e:
    print("Error:", e)