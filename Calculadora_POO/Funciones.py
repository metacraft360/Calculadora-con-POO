class Calculadora():
    def __init__(self):
        pass
    
    def suma(self):
        a = True
        while a:
            try:
                n1 =  int(input("Dime el número 1\n"))
                n2 = int(input("Dime el numero 2\n"))
                print(f"El resultado es: {n1+n2}")
                pass
            except ValueError:
                print("Elige numeros")
    def resta(self):
        a = True
        while a:
            try:
                n1 =  int(input("Dime el número 1\n"))
                n2 = int(input("Dime el numero 2\n"))
                print(f"El resultado es: {n1-n2}")
                pass
            except ValueError:
                print("Elige numeros")
    def multiplicacion(self):
        a = True
        while a:
            try:
                n1 =  int(input("Dime el número 1\n"))
                n2 = int(input("Dime el numero 2\n"))
                print(f"El resultado es: {n1*n2}")
                pass
            except ValueError:
                print("Elige numeros")
    def division(self):
        a = True
        while a:
            try:
                n1 =  int(input("Dime el número 1\n"))
                n2 = int(input("Dime el numero 2\n"))
                print(f"El resultado es: {n1/n2}")
                pass
            except ValueError:
                print("Elige numeros")
                    