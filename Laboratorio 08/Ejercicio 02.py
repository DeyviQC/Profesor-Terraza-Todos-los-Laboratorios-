
import random
import string

def generador_contraseña(longitud):
    # Define los conjuntos de caracteres para generar la contraseña
    letras_minusculas = string.ascii_lowercase
    letras_mayusculas = string.ascii_uppercase
    digitos = string.digits
    caracteres_especiales = '!@#$%^&*()_+-=[]{}|;:,.<>?'

    # Asegura que la longitud de la contraseña sea al menos 8
    if longitud < 8:
        print("La longitud mínima de la contraseña es 8 caracteres.")
        return

    # Asegura que la contraseña cumpla con los requisitos de seguridad
    while True:
        contraseña = ''.join(random.choice(letras_minusculas + letras_mayusculas + digitos + caracteres_especiales) for _ in range(longitud))

        # Revuelve la contraseña aleatoriamente para hacerla más segura
        contraseña = ''.join(random.sample(contraseña, len(contraseña)))

        # Verifica si la contraseña cumple con los requisitos
        if (any(i in letras_minusculas for i in contraseña) and
            any(i in letras_mayusculas for i in contraseña) and
            any(i in digitos for i in contraseña) and
            any(i in caracteres_especiales for i in contraseña)):
            return contraseña

longitud_de_contraseña = int(input("Ingresa la longitud deseada para la contraseña: "))
contraseña = generador_contraseña(longitud_de_contraseña)
print("Contraseña generada:", contraseña)