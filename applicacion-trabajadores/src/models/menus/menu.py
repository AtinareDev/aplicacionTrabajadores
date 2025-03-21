class Menu:
    def __init__(self):
        self.options = {
            1: "Opción 1: Agregar departamento",
            2: "Opción 2: Agregar trabajador",
            3: "Opción 3: Mostrar departamentos",
            4: "Opción 4: Mostrar trabajadores",
            5: "Opción 5: Añadir horas extras",
            6: "Opción 6: Salir"
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
