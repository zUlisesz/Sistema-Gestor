"""Fabrica de conexiones MySQL para la capa de persistencia."""

from .settings import DatabaseSettings


class DatabaseError(RuntimeError):
    """Error controlado al cargar el driver o abrir la base de datos."""


def connect_db(settings=None):
    """Abre una conexion usando configuracion externa y errores explicitos."""
    try:
        import mysql.connector
    except ModuleNotFoundError as error:
        raise DatabaseError(
            "Falta mysql-connector-python. Instala las dependencias del proyecto."
        ) from error

    config = settings or DatabaseSettings.from_env()
    try:
        return mysql.connector.connect(
            host=config.host,
            user=config.user,
            password=config.password,
            database=config.database,
            port=config.port,
        )
    except mysql.connector.Error as error:
        raise DatabaseError(f"No fue posible conectar con la base de datos: {error}") from error
