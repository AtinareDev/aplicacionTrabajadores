import os
def greet():
    print("Bienvenido a la aplicación de trabajadores.")

def calcular_sueldo(base, horas_extra, tarifa_extra):
    """
    Calcula el sueldo total de un trabajador.
    
    :param base: Sueldo base del trabajador.
    :param horas_extra: Horas extra trabajadas.
    :param tarifa_extra: Tarifa por hora extra.
    :return: Sueldo total.
    """
    return base + (horas_extra * tarifa_extra) if horas_extra > 0 else base

def limpiar():
    """
    Limpia la pantalla de la consola.
    """
    os.system('cls' if os.name == 'nt' else 'clear')