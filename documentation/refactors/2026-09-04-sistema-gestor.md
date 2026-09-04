# Refactor de Sistema Gestor

Fecha de creacion: 2026-09-04

## Descripcion

Se refactorizo el proyecto para conservar su arquitectura por capas y reducir
el acoplamiento entre interfaz, casos de uso y persistencia. Se externalizo la
configuracion de MySQL, se agrego manejo explicito de errores de conexion, se
normalizaron los repositorios, se corrigieron entidades con atributos
inseguros o incompletos y se hicieron inyectables los controladores para poder
probarlos sin MySQL. La interfaz dejo de abrir Flet durante la importacion y
dejo de mostrar hashes de contrasena.

## Archivos modificados

- `main.py`
- `models/`
- `repositories/`
- `repositories/student_course_repository.py`
- `services/database.py`
- `services/settings.py`
- `controllers/`
- `views/login_view.py`
- `views/signup_view.py`
- `views/student_view.py`
- `views/teacher_view.py`
- `views/admin_view.py`
- `views/app.py`
- `.env.example`
- `.gitignore`
- `requirements.txt`
- `pyproject.toml`
- `tests/test_core.py`
- `README.md`

## Migracion a Flet app

El frontend ahora usa `ft.run(main)` como entrypoint, `page.navigate()` para
la navegacion sincrona y una clase `ClassroomApp` como unico responsable de
construir `page.views` a partir de `page.route`. Tambien se agrego el manejo de
`page.on_view_pop` para el retroceso y la configuracion `pyproject.toml` para
ejecutar la app con `flet run`.

## Verificacion

- `python3 -m unittest discover -s tests -v`: 4 pruebas superadas.
- Importacion de `main` y de todas las capas: superada.
- Analisis AST de todos los archivos Python: superado.
- `flet run --hidden --directory . --recursive`: arranque desktop superado.
- `flet run --web --directory . --recursive --port 8550`: servidor web levantado.
- `curl -I http://127.0.0.1:8550`: respuesta HTTP 200.

Referencias oficiales consultadas:

- https://flet.dev/docs/getting-started/create-flet-app/
- https://flet.dev/docs/cookbook/navigation-and-routing/
- https://flet.dev/docs/getting-started/running-app/
