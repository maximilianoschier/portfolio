import reflex as rx

from portfolio.components.heading import heading
from portfolio.views.info_detail import info_detail
from portfolio.styles.styles import Size
from portfolio.data import Info

def info(title: str, info: list[Info]) -> rx.Component:
    return rx.vstack(
        heading(title),
        rx.vstack(
            *[
                info_detail(item)
                for item in info
            ],
            spacing=Size.DEFAULT.value,
            width="100%"
        ),              
        spacing=Size.DEFAULT.value,
        width="100%"
    )