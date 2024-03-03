import reflex as rx

from portfolio.components.heading import heading
from portfolio.components.media import media
from portfolio.styles.styles import Size, IMAGE_HEIGHT

def card_detail() -> rx.Component:
    return rx.card(
        rx.inset(
            rx.image(
                src="/favicon.ico",
                height=IMAGE_HEIGHT,
                width="100%",
            ),
            pb=Size.DEFAULT.value
        ),
        rx.text(
            "Description",
            size=Size.SMALL.value,
            color_scheme="gray"
        ),
        width="100%"
    )