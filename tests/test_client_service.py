import pytest

from clientes.models import Cliente
from clientes.services import ServicioClientes


class RepositorioFalso:
    def __init__(self):
        self.guardados = []

    def guardar(self, cliente):
        self.guardados.append(cliente)


class NotificadorFalso:
    def __init__(self):
        self.enviados = []

    def enviar_bienvenida(self, cliente):
        self.enviados.append(cliente)


def crear_servicio():
    repo, notificador = RepositorioFalso(), NotificadorFalso()
    return ServicioClientes(repo, notificador), repo, notificador


def test_registra_cliente_valido():
    servicio, repo, notificador = crear_servicio()
    cliente = Cliente("Ana Pérez", "ana@correo.com")
    servicio.registrar(cliente)
    assert repo.guardados == [cliente]
    assert notificador.enviados == [cliente]


def test_rechaza_nombre_vacio():
    servicio, repo, _ = crear_servicio()
    with pytest.raises(ValueError):
        servicio.registrar(Cliente("   ", "ana@correo.com"))
    assert repo.guardados == []


def test_rechaza_correo_invalido():
    servicio, repo, _ = crear_servicio()
    with pytest.raises(ValueError):
        servicio.registrar(Cliente("Ana Pérez", "correo-sin-arroba"))
    assert repo.guardados == []
