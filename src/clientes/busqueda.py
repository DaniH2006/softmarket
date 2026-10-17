def buscar_por_documento(clientes: list[dict], documento: str) -> dict | None:
    """Devuelve el primer cliente cuyo documento coincide, o None."""
    for cliente in clientes:
        if cliente.get("documento") == documento:
            return cliente
    return None
