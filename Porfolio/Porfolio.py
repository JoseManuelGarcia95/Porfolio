import reflex as rx
from .state import BookState

def BookComponent():
    return rx.box(
            rx.box(
                rx.heading(BookState.current_title, class_name="chapter-title"),
                rx.text(BookState.current_content, class_name="chapter-content"),
                class_name=rx.cond(BookState.is_flipping, "book-page flipping", "book-page"),
        ),
        rx.hstack(
            rx.button("Anterior", on_click=BookState.previous_page, disabled=BookState.current_page == 0),
            rx.button("Siguiente", on_click=BookState.next_page, disabled=BookState.current_page == BookState.total_pages -1),
            spacing="4",
            justify="center",
            margin_top="1em",
        ),
        class_name="book-container"
    )

def index():
    return rx.box(
        BookComponent(),
        class_name="main-container"
    )

app = rx.App()
app.add_page(index, title="Porfolio-JMGA")

app.stylesheets.append("main.css")