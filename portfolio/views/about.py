import reflex as rx

from portfolio.components.heading import heading

def about() -> rx.Component:
    return rx.vstack(
        heading("About me"),
        rx.text("Description")
    )