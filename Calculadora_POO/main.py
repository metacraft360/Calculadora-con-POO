from pathlib import Path
from Funciones import Calculadora, Usuario
import json
mi_calculadora = Calculadora()
mi_usuairo = Usuario()
programa = True
datos_correctos = None

while programa:
    try:
        elegir_accion = int(input("Que quieres hacer, (1) registrarse, (2) iniciar sesion\n"))
        if elegir_accion == 1:
            mi_usuairo.registro()
        elif elegir_accion == 2:
            datos_correctos = mi_usuairo.inicio_sesion(datos_correctos)
            try:
                if datos_correctos[0] == True:
                    programa = False
                else:
                    programa = True
            except json.JSONDecodeError:
                print("No hay ninguna cuenta creada")
        else:
            print("Elige entre 1-2")

    except ValueError:
        print("Elige entre 1-2")

print(f"Bienvenido a la calculadora, {datos_correctos[1]}")
a = True

while a:
    try:
        accion = int(input("(1)Suma,(2)Resta,(3)Multiplicacion,(4)Division,(5)Raiz cuadrada\n"))
        if accion == 1:
            mi_calculadora.suma()
        elif accion == 2:
            mi_calculadora.resta()
        elif accion == 3:
            mi_calculadora.multiplicacion()
        elif accion == 4:
            mi_calculadora.division()
        elif accion == 5:
            mi_calculadora.raiz()
        else:
            print("Elige entre 1-4")
        pass
    except ValueError:
        print("Elige entre 1-4")


