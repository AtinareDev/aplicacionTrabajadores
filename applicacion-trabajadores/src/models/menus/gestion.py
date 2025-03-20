from .menu import Menu
from ..trabajador import Trabajador
from ..departamento import Departamento
from utils.helpers import limpiar

class Gestion:
    def __init__(self):
        self.menu = Menu()

    def run(self):
        while True:
            self.menu.display()
            choice = self.menu.get_choice()
            if choice == 1:
                print(f"Usted ha seleccionado la opción {choice}.")
                self.mostrar_trabajadores()
            elif choice == 2:
                print(f"Usted ha seleccionado la opción {choice}.")
                self.mostrar_departamentos()
            elif choice == 3:
                print(f"Usted ha seleccionado la opción {choice}.")
                self.agregar_trabajador()
            elif choice == 4:
                print(f"Usted ha seleccionado la opción {choice}.")
                self.agregar_departamento()
            elif choice == 5:
                print(f"Usted ha seleccionado la opción {choice}.")
                self.calcular_sueldo()
            elif choice == 6:
                print(f"Usted ha seleccionado la opción {choice}.")
                self.mostrar_informacion()
            elif choice == 7:
                print(f"Usted ha seleccionado la opción {choice}.")
                print("Saliendo del programa...")
                break

    def mostrar_trabajadores(self):
        print("Mostrando trabajadores...")
        with open(r"datos\trabajadores.txt", "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            print(contenido)

    def mostrar_departamentos(self):
        print("Mostrando departamentos...")
        with open(r"datos\departamentos.txt", "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            limpiar()
            print(contenido)

    def agregar_trabajador(self):
        print("Agregando trabajador...")

        # Obtener datos del trabajador
        nombre = input("Ingrese el nombre del trabajador: ")
        apellido = input("Ingrese el apellido del trabajador: ")
        edad = input("Ingrese la edad del trabajador: ")
        departamento = input("Ingrese el departamento del trabajador: ")

        # Buscar el sueldo en departamentos.txt
        sueldo = None
        with open(r"datos\departamentos.txt", "r", encoding="utf-8") as archivo_departamentos:
            for linea in archivo_departamentos:
                # Suponemos que cada línea tiene formato "Departamento, sueldo"
                dept, sueldo_departamento = linea.strip().split(",")
                if dept.strip().lower() == departamento.lower():  # Comparar sin distinguir mayúsculas
                    sueldo = sueldo_departamento.strip()
                    break
        
        if sueldo:
            # Si encontramos el sueldo, lo asignamos al trabajador
            trabajador = Trabajador(nombre, apellido, edad, departamento)
            # Escribir el trabajador en trabajadores.txt
            with open(r"datos\trabajadores.txt", "a", encoding="utf-8") as archivo_trabajadores:
                archivo_trabajadores.write(f"{trabajador} - Sueldo: {sueldo}\n")
            print(f"Trabajador {nombre} {apellido} agregado al departamento {departamento} con un sueldo de {sueldo}.")
        else:
            limpiar()
            print(f"No se encontró el departamento {departamento}. Por favor, verifica el nombre del departamento.")



    def agregar_departamento(self):
        print("Agregando departamento...")
        # Implementar lógica para agregar departamento

    def calcular_sueldo(self):
        print("Calculando sueldo...")
        # Implementar lógica para calcular sueldo

    def mostrar_informacion(self):
        print("Mostrando información...")
        # Implementar lógica para mostrar información
