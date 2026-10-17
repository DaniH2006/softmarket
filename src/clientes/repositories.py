from clientes.models import Cliente


class RepositorioEnMemoria:
    """Implementación simple, útil para pruebas y demostraciones."""

    def __init__(self) -> None:
        self._clientes: list[Cliente] = []

    def guardar(self, cliente: Cliente) -> None:
        self._clientes.append(cliente)

    def listar(self) -> list[Cliente]:
        return list(self._clientes)


class RepositorioSQL:
    def __init__(self, conexion) -> None:
        self._conexion = conexion

    def guardar(self, cliente: Cliente) -> None:
        self._conexion.execute(
            "INSERT INTO clientes (nombre, correo) VALUES (?, ?)",
            (cliente.nombre, cliente.correo),
        )
        self._conexion.commit()
