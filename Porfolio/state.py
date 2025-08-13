import reflex as rx

class BookState(rx.State):
    pages = [
        {"title": "Portada", "content": "Bienvenidos a mi portfolio."},
        {"title": "Sobre mí", "content": "Soy José Manuel, desarrollador con pasión por crear soluciones eficientes."},
        {"title": "Habilidades", "content": "Python, JavaScript, React, Reflex, HTML, CSS..."},
        {"title": "Proyectos", "content": "Listado de mis proyectos más relevantes con detalles técnicos."},
        {"title": "Experiencia", "content": "Mi experiencia profesional y académica."},
        {"title": "Contacto", "content": "¿Listo para trabajar juntos? Escríbeme."}
    ]
    current_page: int = 0
    is_flipping: bool = False

    #Navegación
    def next_page(self):
        if self.current_page < len(self.pages) -1:
            self.is_flipping = True
            yield
            self.current_page += 1
            self.is_flipping = False

    def previous_page(self):
        if self.current_page > 0:
            self.is_flipping = True
            yield
            self.current_page -= 1
            self.is_flipping = False

    def jump_to_page(self, page_number: int):
        if 0 <= page_number < self.total_pages:
            self.current_page = page_number

    #Propiedades reactivas
    @rx.var
    def total_pages(self) -> int:
        return len(self.pages)

    @rx.var
    def current_title(self) -> str:
        return self.pages[self.current_page]["title"]

    @rx.var
    def current_content(self) -> str:
        return self.pages[self.current_page]["content"]
