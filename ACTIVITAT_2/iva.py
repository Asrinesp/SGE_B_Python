salario = float(input("Cual es tu salario? "))

if salario <= 15000:
    print("Tu salario con el IVA es el mismo")
elif salario <= 30000:
    print(f"Tu salario con IVA es {salario * 10/100}")
elif salario <= 60000:
    print(f"Tu salario con IVA es {salario * 21/100}")
else:
    print("Introduce un numero entre el 0 y el 60.000")