import reflex as rx
from Porfolio.state import BookState

def BookComponent() -> rx.Component:
    return rx.vstack(
        rx.box(
            rx.box(
                rx.heading(BookState.current_title, size="1"),
                rx.text(BookState.current_content),
                padding="2em",
                class_name=rx.cond(
                    BookState.is_flipping,
                    "page flipping",
                    "page"
                )
            ),
            class_name="book",
            height="100vh",
            widht="100%",
        ),
        rx.hstack(
            rx.button(
                "← Anterior",
                on_click=BookState.previous_page,
                class_name="nav-button",
                is_disabled=BookState.current_page == 0,
            ),
            rx.text(
                f"Página {BookState.current_page + 1} de {BookState.total_pages}",
                class_name="page-number"
            ),
            rx.button(
                "Siguiente →",
                on_click=BookState.next_page,
                class_name="nav-button",
                is_disabled=BookState.current_page == BookState.total_pages - 1,
            ),
            class_name="book-controls",
            position="fixed",
            bottom="2em",
            z_index="1000"
        ),
        class_name="book-container",
        width="100%",
        height="100vh",
        overflow="hidden"
    )

def index() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading("Porfolio de José Manuel García", size="9", margin_bottom="1em"),
            BookComponent(),
            width="100%",
            max_width="1200px",
            min_height="100vh",
            padding="0",
            spacing="0",
        ),
        width="100%",
        height="100vh"
    )

app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&display=swap",
        "styles/main.css"
    ]
)
app.add_page(index)