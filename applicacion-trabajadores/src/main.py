from models.trabajador import Trabajador
from models.departamento import Departamento
from models.menus.menu import Menu
from models.menus.gestion import Gestion
from utils.helpers import greet


def saludo():
    greet()


if __name__ == "__main__":
    saludo()
    gestion = Gestion()
    gestion.run()
