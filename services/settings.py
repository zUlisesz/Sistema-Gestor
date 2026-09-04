"""Configuracion de infraestructura cargada desde variables de entorno."""

from dataclasses import dataclass
import os


@dataclass(frozen=True)
class DatabaseSettings:
    host: str = "127.0.0.1"
    user: str = "root"
    password: str = ""
    database: str = "gestor"
    port: int = 3306

    @classmethod
    def from_env(cls):
        return cls(
            host=os.getenv("GESTOR_DB_HOST", cls.host),
            user=os.getenv("GESTOR_DB_USER", cls.user),
            password=os.getenv("GESTOR_DB_PASSWORD", ""),
            database=os.getenv("GESTOR_DB_NAME", cls.database),
            port=int(os.getenv("GESTOR_DB_PORT", str(cls.port))),
        )
