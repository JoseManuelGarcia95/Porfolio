import reflex as rx
from .state import BookState

def book_cover():
    """Portada del libro con diseño especial"""
    return rx.box(
        rx.vstack(
            rx.box(
                rx.heading("JOSÉ MANUEL GARCÍA", size="9", color="#8B4513", font_weight="bold"),
                rx.heading("Desarrollador Web", size="6", color="#A0522D", margin_top="1rem"),
                rx.divider(margin_y="2rem", border_color="#D2B48C", height="2px"),
                rx.text("Portfolio Personal - Desarrollo Web con Python & IA", 
                       font_size="1.2rem", color="#654321", font_style="italic", text_align="center"),
                rx.spacer(),
                rx.vstack(
                    rx.text("Python • Reflex • Angular • IA", 
                           font_size="1rem", color="#A0522D", font_weight="500"),
                    rx.text("Análisis de Datos • APIs • Interfaces Modernas", 
                           font_size="0.9rem", color="#8B4513"),
                    spacing="1",
                    align="center"
                ),
                text_align="center"
            ),
            spacing="2",
            height="100%",
            justify="center"
        ),
        class_name="book-cover"
    )

def table_of_contents():
    """Índice del libro"""
    return rx.vstack(
        rx.heading("Índice", size="7", color="#8B4513", margin_bottom="2rem", text_align="center"),
        rx.vstack(
            rx.hstack(
                rx.text("Capítulo 1:", font_weight="bold"),
                rx.text("Sobre Mí"),
                rx.spacer(),
                rx.text("3", font_family="monospace"),
                width="100%",
                align="center",
                class_name="index-item"
            ),
            rx.hstack(
                rx.text("Capítulo 2:", font_weight="bold"),
                rx.text("Habilidades Técnicas"),
                rx.spacer(),
                rx.text("4", font_family="monospace"),
                width="100%",
                align="center",
                class_name="index-item"
            ),
            rx.hstack(
                rx.text("Capítulo 3:", font_weight="bold"),
                rx.text("Proyectos Destacados"),
                rx.spacer(),
                rx.text("5", font_family="monospace"),
                width="100%",
                align="center",
                class_name="index-item"
            ),
            rx.hstack(
                rx.text("Capítulo 4:", font_weight="bold"),
                rx.text("Experiencia Profesional"),
                rx.spacer(),
                rx.text("6", font_family="monospace"),
                width="100%",
                align="center",
                class_name="index-item"
            ),
            rx.hstack(
                rx.text("Capítulo 5:", font_weight="bold"),
                rx.text("Conectemos"),
                rx.spacer(),
                rx.text("7", font_family="monospace"),
                width="100%",
                align="center",
                class_name="index-item"
            ),
            spacing="2",
            width="100%"
        ),
        spacing="2",
        class_name="table-of-contents"
    )

def chapter_page():
    """Página normal de capítulo"""
    return rx.vstack(
        rx.hstack(
            rx.text(f"Capítulo {BookState.current_page - 1}", 
                   font_size="0.9rem", color="#8B4513", font_weight="500"),
            rx.spacer(),
            rx.text(f"Página {BookState.current_page + 1}", 
                   font_size="0.9rem", color="#8B4513"),
            width="100%",
            margin_bottom="1.5rem"
        ),
        rx.heading(BookState.current_title, size="7", color="#8B4513", margin_bottom="1.5rem"),
        rx.box(
            rx.text(BookState.current_content, line_height="1.6", text_align="justify"),
            flex="1"
        ),
        height="100%",
        spacing="2"
    )

def page_navigation():
    """Navegación entre páginas mejorada"""
    return rx.hstack(
        rx.button(
            rx.hstack(
                rx.icon("chevron-left", size=16),
                rx.text("Anterior"),
                spacing="1"
            ),
            on_click=BookState.prev_page,
            disabled=BookState.current_page == 0,
            variant="soft",
            color_scheme="brown",
            class_name="nav-button"
        ),
        rx.hstack(
            rx.text(f"{BookState.current_page + 1}", font_weight="bold"),
            rx.text("de"),
            rx.text(f"{BookState.total_pages}", font_weight="bold"),
            spacing="1",
            font_size="0.9rem",
            color="#8B4513"
        ),
        rx.button(
            rx.hstack(
                rx.text("Siguiente"),
                rx.icon("chevron-right", size=16),
                spacing="1"
            ),
            on_click=BookState.next_page,
            disabled=BookState.current_page == BookState.total_pages - 1,
            variant="soft",
            color_scheme="brown",
            class_name="nav-button"
        ),
        justify="between",
        width="100%",
        align="center"
    )

def book_spine():
    """Simula el lomo del libro"""
    return rx.box(
        rx.text("JOSÉ MANUEL GARCÍA", 
               writing_mode="vertical-rl", 
               text_orientation="mixed",
               font_weight="bold",
               color="#654321",
               font_size="1.1rem"),
        class_name="book-spine"
    )

def book_component():
    """Componente principal del libro"""
    return rx.center(
        rx.hstack(
            # Lomo del libro (decorativo)
            book_spine(),
            
            # Libro principal
            rx.box(
                # Contenido de la página
                rx.cond(
                    BookState.current_page == 0,
                    book_cover(),
                    rx.cond(
                        BookState.current_page == 1,
                        table_of_contents(),
                        chapter_page()
                    )
                ),
                class_name="book-page"
            ),
            
            # Sombra del libro
            rx.box(class_name="book-shadow"),
            
            spacing="0"
        ),
        
        # Navegación
        rx.box(
            page_navigation(),
            class_name="navigation-container"
        ),
        
        class_name="book-container",
        min_height="100vh"
    )

def index():
    return book_component()

app = rx.App()
app.add_page(index)
app.stylesheets.append("main.css")