import json
import math
from pathlib import Path

carpeta_src = Path(__file__).parent
localizacion_json = carpeta_src / ".." / "Calculadora_POO"/"almacenamiento" / "archivo.json"

class Usuario():
    def __init__(self, ruta_archivo=localizacion_json):
        self.ruta_json = ruta_archivo
    def registro(self):
        correo_comprobacion = True
        contraseña_comprobacion = True
        nombre_usuario = input("Dime tu nombre de usuario\n")
        while correo_comprobacion:
            correo_electrónico = input("Dime tu correo electrónico\n")
            if "@" in correo_electrónico:
                correo_comprobacion = False
            else:
                print("Tu correo electrónico necesita una arroba (@)")
        while contraseña_comprobacion:
            contraseña = input("Dime tu contraseña\n")
            if len(contraseña) <= 4:
                print("La contraseña es muy pequeña, escoge otra")
            else:
                print("La contraseña es válida")
                confirmar_contraseña = input("Vuelve a escribir la contraseña\n")
                if confirmar_contraseña == contraseña:
                    print("La contraseña es válida")
                    contraseña_comprobacion = False
                else:
                    print("La contraseña no es igual, repite el proceso")

        datos_usuario = {}
        with open(self.ruta_json, "r", encoding="utf-8") as archivo:
            datos_usuario = json.load(archivo)

        if nombre_usuario in datos_usuario:
            print("Esa cuenta ya ha sido registrada, crea otra")
        else:
            datos_usuario[nombre_usuario] = [correo_electrónico, contraseña]
            with open(self.ruta_json, "w") as archivo:
                json.dump(datos_usuario, archivo, indent=4)
                print("Cuenta creado correctamente")


    def inicio_sesion(self,datos_correctos):
        datos_usuario = {}
        datos = {}
        correo_comprobacion = True
        contraseña_comprobacion = True
        with open(self.ruta_json, "r") as archivo:
            datos_usuario = json.load(archivo)
        nombre_usuario = input("Dime tu nombre de usuario\n")
        while correo_comprobacion:
            correo_electrónico = input("Dime tu correo electrónico\n")
            if "@" in correo_electrónico:
                correo_comprobacion = False
            else:
                print("Tu correo electrónico necesita una arroba (@)")
        contraseña = input("Dime tu contraseña\n")

        if nombre_usuario in datos_usuario:
            if contraseña in datos_usuario[nombre_usuario] and correo_electrónico in datos_usuario[nombre_usuario]:
                print("Iniciando sesión 。。。")
                datos_correctos = True
                return datos_correctos, nombre_usuario
            else:
                print("Esa cuenta no existe")
                datos_correctos = False
                return datos_correctos, nombre_usuario
                
        else:
            print("Esa cuenta no existe")
            datos_correctos = False
            return datos_correctos, nombre_usuario

        
    


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
                a = False
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
                a = False
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
                a = False
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
                a = False
                pass
            except ValueError:
                print("Elige numeros")
    def raiz(self):
            a = True
            while a:
                try:
                    n1 =  int(input("Dime el número a operar\n"))
                    print(f"El resultado es: {math.sqrt(n1)}")
                    a = False
                    pass
                except ValueError:
                    print("Elige numeros")
                    