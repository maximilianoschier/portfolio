import reflex as rx

from portfolio.components.heading import heading
from portfolio.views.info_detail import info_detail
from portfolio.styles.styles import Size

def info(title: str) -> rx.Component:
    return rx.vstack(
        heading(title),
        info_detail(),
        spacing=Size.DEFAULT.value,
        width="100%"
    )