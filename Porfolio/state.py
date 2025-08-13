import reflex as rx

class BookState(rx.State): 
    # Variables reactivas (que pueden cambiar)
    current_page: int = 0
    total_pages: int = 6
    is_flipping: bool = False

    # Datos fijos
    page_titles: list[str] = [
        "Portada",
        "Sobre mí",
        "Habilidades",
        "Proyectos",
        "Experiencia",
        "Contacto",
    ]

    page_content: dict[str, str] = {
        "Portada": "Bienvenidos a mi portfolio",
        "Sobre mí": "Soy José Manuel...",
        "Habilidades": "Python, React, JavaScript...",
        "Proyectos": "Mis proyectos más destacados...",
        "Experiencia": "Mi experiencia profesional...",
        "Contacto": "¿Listo para trabajar juntos?",
    }

    # Métodos para cambiar de página
    def next_page(self):
        if self.current_page < self.total_pages - 1 and not self.is_flipping:
            self.is_flipping = True
            self.current_page += 1
            self.is_flipping = False

    def previous_page(self):
        if self.current_page > 0 and not self.is_flipping:
            self.is_flipping = True
            self.current_page -= 1
            self.is_flipping = False

    def jump_to_page(self, page_number: int):
        if 0 <= page_number < self.total_pages:
            self.current_page = page_number

    # Propiedades reactivas
    @rx.var
    def current_title(self) -> str:
        return self.page_titles[self.current_page]

    @rx.var
    def current_content(self) -> str:
        return self.page_content[self.page_titles[self.current_page]]
