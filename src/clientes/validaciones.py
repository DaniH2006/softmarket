def correo_duplicado(correo: str, existentes: list[str]) -> bool:
    """Indica si el correo ya está registrado (sin distinguir mayúsculas)."""
    return correo.strip().lower() in {c.strip().lower() for c in existentes}
