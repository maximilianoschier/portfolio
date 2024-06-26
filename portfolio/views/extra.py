import reflex as rx

from portfolio.components.heading import heading
from portfolio.components.card_detail import card_detail
from portfolio.styles.styles import Size
from portfolio.data import Extra

def extra(extras: list[Extra]) -> rx.Component:
    return rx.vstack(
        heading("Extra"),
        rx.mobile_only(
            rx.vstack(
                *[
                    card_detail(extra)
                    for extra in extras
                ],
                spacing=Size.DEFAULT.value,  
            ),
            width="100%"
        ),
        rx.tablet_and_desktop(
            rx.grid(
                *[
                    card_detail(extra)
                    for extra in extras
                ],
                spacing=Size.DEFAULT.value,
                columns="3"
            ),
            width="100%"
        ),
        spacing=Size.DEFAULT.value,
        width="100%"
    )
