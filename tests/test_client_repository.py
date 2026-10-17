import sqlite3

from clientes.models import Cliente
from clientes.repositories import RepositorioEnMemoria, RepositorioSQL


def test_repositorio_en_memoria_guarda_y_lista():
    repo = RepositorioEnMemoria()
    cliente = Cliente("Ana Pérez", "ana@correo.com")
    repo.guardar(cliente)
    assert repo.listar() == [cliente]


def test_repositorio_sql_guarda_y_recupera():
    conexion = sqlite3.connect(":memory:")
    conexion.execute("CREATE TABLE clientes (nombre TEXT, correo TEXT)")
    RepositorioSQL(conexion).guardar(Cliente("Ana Pérez", "ana@correo.com"))
    filas = conexion.execute("SELECT nombre, correo FROM clientes").fetchall()
    assert filas == [("Ana Pérez", "ana@correo.com")]
