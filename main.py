"""Punto de entrada de Sistema-Gestor."""

import flet as ft

from views.login_view import main


if __name__ == "__main__":
    ft.app(target=main)
#por último dentro del archivo main se importa el módulo con la vista principal para que ejecute todo el programa
