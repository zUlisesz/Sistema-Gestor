# Sistema Gestor

Aplicacion de escritorio para gestionar usuarios, cursos, inscripciones y
avisos por rol: administrador, profesor y estudiante.

## Arquitectura

- `views/`: interfaz Flet y eventos de usuario.
- `controllers/`: casos de uso y reglas de coordinacion.
- `repositories/`: acceso parametrizado a MySQL.
- `models/`: entidades del dominio.
- `services/`: configuracion y servicios de infraestructura.
- `tests/`: pruebas unitarias sin necesidad de una base de datos real.

## Ejecucion

1. Instala dependencias con `python -m pip install -r requirements.txt`.
2. Define en tu entorno las variables de `.env.example` (puedes usar ese
   archivo como plantilla).
3. Ejecuta `python main.py` desde esta carpeta.

La configuracion se lee desde `GESTOR_DB_HOST`, `GESTOR_DB_USER`,
`GESTOR_DB_PASSWORD`, `GESTOR_DB_NAME` y `GESTOR_DB_PORT`. La aplicacion ya no
contiene credenciales dentro del codigo.

## Pruebas

```bash
python -m unittest discover -s tests -v
```

El ejecutable y el video originales estan disponibles en el
[enlace del proyecto](https://drive.google.com/drive/folders/10HgYdZ4ZtwRUo8Sz9LINvQEj0xvGEWMu?usp=sharing).

La app sigue el punto de entrada `main.py` de Flet y puede ejecutarse también
con `flet run` o `flet run --web`.
