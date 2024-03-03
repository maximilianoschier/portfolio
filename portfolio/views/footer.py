import reflex as rx

from portfolio.components.heading import heading
from portfolio.components.media import media
from portfolio.styles.styles import Size

def footer() -> rx.Component:
    return rx.vstack(
        rx.text("Nombre"),
        media(),
        spacing=Size.SMALL.value
    )