from itertools import repeat

nota = float(input("Que nota tienes? "))

if (nota > 0 and nota <= 4.99):
    print("El alumno a suspendido")
elif nota <= 6.5:
    print("El alumno a aprovado")
elif nota <= 8:
    print("El alumno ha sacado un notable")
elif nota <= 10:
    print("El alumno ha sacado un Excelente, ¡enhorabuena! :)")
else:
    print("Introduce una nota valida fel 1-10")