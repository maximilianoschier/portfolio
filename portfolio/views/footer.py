import reflex as rx

from portfolio.components.heading import heading
from portfolio.components.media import media
from portfolio.styles.styles import Size
from portfolio.data import Media

def footer(data: Media) -> rx.Component:
    return rx.vstack(
        rx.text("Nombre"),
        media(data),
        spacing=Size.SMALL.value
    )