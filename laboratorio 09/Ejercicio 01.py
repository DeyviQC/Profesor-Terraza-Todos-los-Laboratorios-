def celsius_a_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

try:
    temperatura = float(input("Ingrese la temperatura: "))
    unidad = input("Ingrese la unidad de temperatura (C o F): ").upper()

    if unidad == "C":
        temperatura_convertida = celsius_a_fahrenheit(temperatura)
        print(temperatura,"°C equivale a",temperatura_convertida ,"°F")
    elif unidad == "F":
        temperatura_convertida = fahrenheit_a_celsius(temperatura)
        print(temperatura," °F equivale a " ,temperatura_convertida,"°C")
    else:
        print("Unidad no válida. Ingrese 'C' para Celsius o 'F' para Fahrenheit.")

except ValueError:
    print("Error: Ingrese una temperatura válida.")