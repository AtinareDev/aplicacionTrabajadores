class Trabajador:
    def __init__(self, nombre, apellido, edad, departamento):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.departamento = departamento

    def __str__(self):
        # Esta es una forma de representar el trabajador como una cadena
        return f"{self.nombre} {self.apellido} ({self.edad} años) {self.departamento}"