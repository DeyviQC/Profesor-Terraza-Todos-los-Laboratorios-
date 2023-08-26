palabra=str(input("Ingrese su palabra palindroma: "))
pali=palabra[::-1]
if palabra==pali:
   print(True)
   print("La palabra",palabra,"es palindroma")
else:
    print(False)
    print("La palabra",palabra,"NO es palindroma")
    