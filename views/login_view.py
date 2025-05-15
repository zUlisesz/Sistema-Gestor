import flet as ft

def login(page: ft.Page):
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.vertical_alignment = ft.CrossAxisAlignment.CENTER
    
    page.theme_mode = ft.ThemeMode.DARK
    
    page.add(
        ft.TextField(label= 'TU CORREO'),
        ft.TextField(label = 'TU CONTRASEÑA'),
        ft.ElevatedButton('INICIAR SECIÖN', elevation= 8)
    )

ft.app( target= login)