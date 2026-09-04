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
- `.env.example`
- `.gitignore`
- `requirements.txt`
- `tests/test_core.py`
- `README.md`
