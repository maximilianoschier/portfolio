import reflex as rx

from portfolio.views.header import header
from portfolio.views.footer import footer
from portfolio.views.about import about
from portfolio.views.info import info
from portfolio.views.tech_stack import tech_stack
from portfolio.views.extra import extra
from portfolio.styles.styles import MAX_WIDTH, EmSize, Size

def index() -> rx.Component:
    return rx.center(
        # rx.theme_panel(),
        rx.vstack(
            header(),
            about(),
            rx.divider(),
            tech_stack(),
            info("Experience"),
            info("Projects"),
            info("Studies"),
            extra(),
            rx.divider(),
            footer(),
            spacing=Size.MEDIUM.value,
            padding_y=EmSize.BIG.value,
            max_width=MAX_WIDTH,
            width="100%"
        )
    )


app = rx.App()
app.add_page(index)
