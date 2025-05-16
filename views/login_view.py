import flet as ft

def login(page: ft.Page):
    
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme = ft.ThemeMode.DARK
    page.title = 'INICIO DE SECIÓN'
    
    email = ft.TextField(label = 'Correo electrónico', width= 360)
    password = ft.TextField(label = 'Contraseña', width= 360)
    
    page.add(email)
    
ft.app(target= login)