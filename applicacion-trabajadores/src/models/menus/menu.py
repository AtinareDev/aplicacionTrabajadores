class Menu:
    def __init__(self):
        self.options = {
            1: "Opción 1: Mostrar trabajadores",
            2: "Opción 2: Mostrar departamentos",
            3: "Opción 3: Agregar trabajador",
            4: "Opción 4: Agregar departamento",
            5: "Opción 5: Calcular sueldo",
            6: "Opción 6: Mostrar información",
            7: "Opción 7: Salir"
        }

    def display(self):
        print("===== Menú =====")
        for key, value in self.options.items():
            print(f"{key}. {value}")
        print("================")

    def get_choice(self):
        while True:
            try:
                choice = int(input("Seleccione una opción: "))
                if choice in self.options:
                    return choice
                else:
                    print("Opción no válida. Intente de nuevo.")
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número.")
