import reflex as rx

from portfolio.components.heading import heading
from portfolio.components.media import media
from portfolio.styles.styles import Size
from portfolio.data import Data

def header(data: Data) -> rx.Component:
    return rx.hstack(
        rx.avatar(
            src=data.avatar,
            size=Size.BIG.value
            ),
        rx.vstack(
            heading(data.name, True),
            heading(data.title),
            rx.text(
                rx.icon("map-pin"),
                data.location,
                display="inherit"
            ),
            media(data.media),
            spacing=Size.SMALL.value,
           
        ),
        spacing=Size.DEFAULT.value,
        
    )