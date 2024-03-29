import reflex as rx

from portfolio.views.header import header
from portfolio.views.footer import footer
from portfolio.views.about import about
from portfolio.views.info import info
from portfolio.views.tech_stack import tech_stack
from portfolio.views.extra import extra
from portfolio.styles.styles import MAX_WIDTH, EmSize, Size, BASE_STYLE, STYLESHEETS
from portfolio import data

DATA = data.data


def index() -> rx.Component:
    return rx.center(
        # rx.theme_panel(),
        rx.vstack(
            header(DATA),
            about(DATA.about),
            rx.divider(),
            tech_stack(DATA.technologies),
            info("Experience", DATA.experience),
            info("Projects", DATA.projects),
            info("Studies", DATA.training),
            extra(DATA.extras),
            rx.divider(),
            footer(DATA.media),
            spacing=Size.MEDIUM.value,
            padding_x=EmSize.MEDIUM.value,
            padding_y=EmSize.BIG.value,
            max_width=MAX_WIDTH,
            width="100%"
        )
    )


app = rx.App(
        stylesheets=STYLESHEETS,
        style=BASE_STYLE,
        theme=rx.theme(
            appearance="light", 
            has_background=True, 
            radius="full",
            grayColor="mauve",
            accent_color="teal"
        )
    )

title = DATA.title
description = DATA.description
image = DATA.image

app.add_page(
    index,
    title=title,
    description=description,
    image=image,
    meta=[
        {"name": "og:title", "content": title},
        {"name": "og:description", "content": description},
        {"name": "og:image", "content": image}
    ]
)