import reflex as rx

from portfolio.components.heading import heading
from portfolio.components.media import media
from portfolio.styles.styles import Size

def tech_stack() -> rx.Component:
    return rx.vstack(
        heading("Tecnologies"),
        rx.flex(
                *[
                    rx.badge(
                        rx.icon("code"),
                        rx.text(f"Stack{index}"),
                        size="2"
                    )
                    for index in range(0, 10)
                ],
                wrap="wrap",
                spacing=Size.SMALL.value,
            ),
            spacing=Size.DEFAULT.value
    )