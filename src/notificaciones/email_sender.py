import smtplib
from email.message import EmailMessage

from clientes.models import Cliente


class NotificadorSMTP:
    def __init__(self, host: str, remitente: str) -> None:
        self._host = host
        self._remitente = remitente

    def enviar_bienvenida(self, cliente: Cliente) -> None:
        mensaje = EmailMessage()
        mensaje["From"] = self._remitente
        mensaje["To"] = cliente.correo
        mensaje["Subject"] = "Bienvenido a SoftMarket"
        mensaje.set_content(f"Hola {cliente.nombre}, ¡bienvenido a SoftMarket!")
        with smtplib.SMTP(self._host) as servidor:
            servidor.send_message(mensaje)
