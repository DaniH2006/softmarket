# Arquitectura

## Módulos y responsabilidades
| Módulo | Responsabilidad |
|---|---|
| `clientes/models.py` | Entidad `Cliente`. |
| `clientes/services.py` | Caso de uso `ServicioClientes`: valida y coordina. Define los contratos `RepositorioClientes` y `Notificador`. |
| `clientes/repositories.py` | Implementaciones de persistencia (`RepositorioSQL`, `RepositorioEnMemoria`). |
| `notificaciones/email_sender.py` | Implementación de notificación por correo (`NotificadorSMTP`). |

## Dependencias
`ServicioClientes` depende de contratos (Protocol), no de SQL ni SMTP. Las implementaciones
concretas se inyectan por constructor desde la configuración de la aplicación.

```
ServicioClientes --> RepositorioClientes <|-- RepositorioSQL / RepositorioEnMemoria
                 --> Notificador         <|-- NotificadorSMTP
```
