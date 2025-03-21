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
            limpiar()
            if choice == 1:
                print(f"Usted ha seleccionado la opción {choice}.")
                self.mostrar_departamentos()
                self.agregar_departamento()
            elif choice == 2:
                print(f"Usted ha seleccionado la opción {choice}.")
                self.agregar_trabajador()
            elif choice == 3:
                print(f"Usted ha seleccionado la opción {choice}.")
                self.mostrar_departamentos()
            elif choice == 4:
                print(f"Usted ha seleccionado la opción {choice}.")
                self.mostrar_trabajadores()
            elif choice == 5:
                print(f"Usted ha seleccionado la opción {choice}.")
                self.calcular_sueldo()
            elif choice == 6:
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
            print(contenido)

    def agregar_trabajador(self):
        print("Agregando trabajador...")

        # Verificar si hay departamentos en el archivo departamentos.txt
        try:
            with open(r"datos\departamentos.txt", "r", encoding="utf-8") as archivo_departamentos:
                contenido = archivo_departamentos.read().strip()
                if not contenido:  # Si el archivo está vacío
                    limpiar()
                    print("No se pueden agregar trabajadores porque no hay departamentos disponibles.")
                    return  # No permitir agregar trabajador
        except FileNotFoundError:
            # Si el archivo no existe, notificar que no se puede agregar trabajador
            limpiar()
            print("No se puede agregar trabajador porque el archivo de departamentos no existe.")
            return  # No permitir agregar trabajador

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
                archivo_trabajadores.write(
                    f"{trabajador} - Sueldo: {sueldo}\n")
            limpiar()
            print(
                f"Trabajador {nombre} {apellido} agregado al departamento {departamento} con un sueldo de {sueldo}.")
        else:
            limpiar()
            print(
                f"No se encontró el departamento {departamento}. Por favor, verifica el nombre del departamento.")
        

    def agregar_departamento(self):
        print("Agregando departamento...")
        # Implementar lógica para agregar departamento
        with open(r"datos\departamentos.txt", "a", encoding="utf-8") as archivo:
            nombre = input("Ingrese el nombre del departamento: ")
            sueldo = input("Ingrese el sueldo del departamento: ")
            archivo.write(f"{nombre}, {sueldo}\n")
            limpiar()
            print(f"Departamento {nombre} agregado con un sueldo de {sueldo}.")

    def calcular_sueldo(self):
        print("Calculando sueldo...")

        # Solicitar al usuario el nombre y apellido del trabajador
        nombre_trabajador = input("Ingrese el nombre del trabajador: ")
        apellido_trabajador = input("Ingrese el apellido del trabajador: ")

        # Solicitar las horas extras y la tarifa extra
        horas_extra = int(input("Ingrese las horas extra trabajadas: "))
        tarifa_extra = float(input("Ingrese la tarifa por hora extra: "))

        # Leer el archivo de trabajadores
        trabajadores_actualizados = []
        trabajador_encontrado = False

        with open(r"datos\trabajadores.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                # Obtener el nombre completo del trabajador, su edad, departamento y sueldo
                partes = linea.strip().split(" - Sueldo: ")
                if len(partes) == 2:
                    trabajador_str = partes[0]
                    sueldo_str = partes[1]

                    # Extraer el nombre y apellido del trabajador
                    trabajador_partes = trabajador_str.split(" (")
                    nombre_apellido = trabajador_partes[0]

                    # Verificar si el trabajador es el que buscamos
                    nombre, apellido = nombre_apellido.split()
                    if nombre.lower() == nombre_trabajador.lower() and apellido.lower() == apellido_trabajador.lower():
                        trabajador_encontrado = True

                        # Calcular el nuevo sueldo
                        sueldo_base = float(sueldo_str.strip())
                        nuevo_sueldo = sueldo_base + \
                            (horas_extra * tarifa_extra)

                        # Actualizar la línea del trabajador con el nuevo sueldo
                        trabajadores_actualizados.append(
                            f"{nombre_apellido} ({trabajador_partes[1]} - Sueldo: {nuevo_sueldo:.2f}\n")
                    else:
                        # Si no es el trabajador que buscamos, mantener la línea original
                        trabajadores_actualizados.append(linea)
                else:
                    trabajadores_actualizados.append(linea)

        if trabajador_encontrado:
            # Si encontramos el trabajador, escribir el archivo con el sueldo actualizado
            with open(r"datos\trabajadores.txt", "w", encoding="utf-8") as archivo:
                archivo.writelines(trabajadores_actualizados)
            limpiar()
            print(
                f"El sueldo del trabajador {nombre_trabajador} {apellido_trabajador} ha sido actualizado correctamente.")
        else:
            limpiar()
            print(
                f"No se encontró al trabajador {nombre_trabajador} {apellido_trabajador}.")
