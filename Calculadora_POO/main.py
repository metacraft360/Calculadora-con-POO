from Funciones import Calculadora
mi_calculadora = Calculadora()

print("Bienvenido a la calculadora")
a = True

while a:
    try:
        accion = int(input("(1)Suma,(2)Resta,(3)Multiplicacion,(4)Division\n"))
        if accion == 1:
            mi_calculadora.suma()
        elif accion == 2:
            mi_calculadora.resta()
        elif accion == 3:
            mi_calculadora.multiplicacion()
        elif accion == 4:
            mi_calculadora.division()
        else:
            print("Elige entre 1-4")
        pass
    except ValueError:
        print("Elige entre 1-4")


