class Departamento:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def __str__(self):
        # Esta es una forma de representar el departamento como una cadena
        return f"{self.nombre} - Sueldo: {self.sueldo}"
