import reflex as rx

class State(rx.State):
    """State of portfolio."""
    pass

def index() -> rx.Component:
    return rx.text("Bienvenido al portfolio de José Manuel")

app = rx.App()
app.add_page(index)