import reflex as rx

from portfolio.components.heading import heading
from portfolio.components.media import media
from portfolio.styles.styles import Size
from portfolio.data import Technology

def tech_stack(technologies: list[Technology]) -> rx.Component:
    return rx.vstack(
        heading("Tecnologies"),
        rx.flex(
                *[
                    rx.badge(
                        rx.box(
                            class_name=technology.icon,
                            font_size="24px"
                        ),
                        rx.text(technology.name),
                        size="2"
                    )
                    for technology in technologies
                ],
                wrap="wrap",
                spacing=Size.SMALL.value,
            ),
            spacing=Size.DEFAULT.value
    )
