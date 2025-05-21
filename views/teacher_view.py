import flet as ft

def main(page: ft.Page):
    page.title = "Panel del Profesor"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.padding = 30 
    page.bgcolor = ft.Colors.WHITE

    # Encabezado
    header = ft.Container(
        content=ft.Row(
            controls=[
                ft.Text("Panel del Profesor", size=24, weight=ft.FontWeight.BOLD),
                #ft.Spacer(),
                ft.Text("Profesor: Juan Pérez"),
                ft.IconButton(icon=ft.Icons.LOGOUT, tooltip="Cerrar sesión")
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        ),
        padding=20,
        bgcolor=ft.Colors.BLUE_100
    )

    # Contenido principal
    content = ft.Container(
        content=ft.Text("Bienvenido al panel del profesor."),
        padding=20,
        expand=True
    )

    # Función para manejar la navegación
    def on_navigation_change(e):
        selected_index = e.control.selected_index
        if selected_index == 0:
            content.content = ft.Text("Vista de Clases")
        elif selected_index == 1:
            content.content = ft.Text("Vista de Tareas")
        elif selected_index == 2:
            content.content = ft.Text("Vista de Estudiantes")
        elif selected_index == 3:
            content.content = ft.Text("Vista de Calendario")
        elif selected_index == 4:
            content.content = ft.Text("Vista de Configuración")
        page.update()

    # Barra lateral de navegación
    navigation = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        destinations=[
            ft.NavigationRailDestination(icon=ft.Icons.CLASS_, label="Clases"),
            ft.NavigationRailDestination(icon=ft.Icons.ASSIGNMENT, label="Tareas"),
            ft.NavigationRailDestination(icon=ft.Icons.GROUP, label="Estudiantes"),
            ft.NavigationRailDestination(icon=ft.Icons.CALENDAR_MONTH, label="Calendario"),
            ft.NavigationRailDestination(icon=ft.Icons.SETTINGS, label="Configuración")
        ],
        on_change=on_navigation_change
    )

    # Estructura de la página
    page.add(
        header,
        ft.Row(
            controls=[
                navigation,
                content
            ],
            expand=True
        )
    )

ft.app(target=main)
