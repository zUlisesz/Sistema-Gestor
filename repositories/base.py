"""Repositorio base con manejo consistente de conexiones y transacciones."""

from services.database import connect_db


class BaseRepository:
    def __init__(self, connection=None):
        self._owns_connection = connection is None
        self.conn = connection if connection is not None else connect_db()
        self.cursor = self.conn.cursor()

    def execute(self, query, parameters=()):
        try:
            self.cursor.execute(query, parameters)
            self.conn.commit()
            return self.cursor.rowcount
        except Exception:
            self.conn.rollback()
            raise

    def get_one(self, query, parameters=()):
        self.cursor.execute(query, parameters)
        return self.cursor.fetchone()

    def get_all(self, query, parameters=()):
        self.cursor.execute(query, parameters)
        return self.cursor.fetchall()

    def close(self):
        if getattr(self, "cursor", None) is not None:
            self.cursor.close()
            self.cursor = None
        if self._owns_connection and getattr(self, "conn", None) is not None:
            self.conn.close()
            self.conn = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
