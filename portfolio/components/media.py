import reflex as rx

from portfolio.styles.styles import Size
from portfolio.components.icon_button import icon_button

def media() -> rx.Component:
    return rx.hstack(
        icon_button(
            "mail",
            "url",
            "maximiliano.schier@gmail.com",
            True
        ),
        icon_button(
            "file-text",
            "url"
        ),
        icon_button(
            "github",
            "url"
        ),
        icon_button(
            "linkedin",
            "url"
        ),
        spacing=Size.SMALL.value
    )