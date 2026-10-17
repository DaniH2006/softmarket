from typing import Protocol

from clientes.models import Cliente


class RepositorioClientes(Protocol):
    def guardar(self, cliente: Cliente) -> None: ...


class Notificador(Protocol):
    def enviar_bienvenida(self, cliente: Cliente) -> None: ...


class ServicioClientes:
    def __init__(self, repo: RepositorioClientes, notificador: Notificador):
        self.repo = repo
        self.notificador = notificador

    def registrar(self, cliente: Cliente) -> None:
        if not cliente.nombre.strip():
            raise ValueError("El nombre es obligatorio")
        if "@" not in cliente.correo:
            raise ValueError("El correo no es válido")
        self.repo.guardar(cliente)
        self.notificador.enviar_bienvenida(cliente)
