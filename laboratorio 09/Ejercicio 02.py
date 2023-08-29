try:
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))
    operacion = input("Ingrese la operación (+, -, *, /): ")

    if operacion == "+":
        resultado = numero1 + numero2
        print("Resultado:", resultado)
    elif operacion == "-":
        resultado = numero1 - numero2
        print("Resultado:", resultado)
    elif operacion == "*":
        resultado = numero1 * numero2
        print("Resultado:", resultado)
    elif operacion == "/":
        if numero2 != 0:
            resultado = numero1 / numero2
            print("Resultado:", resultado)
        else:
            numero2 ==0
            raise ZeroDivisionError ("Error: Divion con 0" )
    else: 
        print("ERROR : Ingrese un operacion valida (+, -, *, /) ")
       
except ZeroDivisionError as e:
    print(e)
except ValueError:
    print("Error: Ingrese numeros válidos.")

