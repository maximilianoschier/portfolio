import reflex as rx

from portfolio.components.heading import heading
from portfolio.components.media import media
from portfolio.styles.styles import Size

def header() -> rx.Component:
    return rx.hstack(
        rx.avatar(size=Size.BIG.value),
        rx.vstack(
            heading("Nombre", True),
            heading("Habilidad principal"),
            rx.text(
                rx.icon("map-pin"),
                "Location",
                display="inherit"
            ),
            media(),
            spacing=Size.SMALL.value,
           
        ),
        spacing=Size.DEFAULT.value,
        
    )