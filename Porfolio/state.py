import reflex as rx

class BookState(rx.State):
    current_page: int = 0
    
    # Páginas del libro con información personal de José Manuel
    pages = [
        {
            "title": "Portada",
            "content": ""
        },
        {
            "title": "Índice",
            "content": ""
        },
        {
            "title": "Sobre Mí",
            "content": """¡Hola! Soy José Manuel 👋

Bienvenido a mi portfolio personal. Soy Desarrollador Web y en este repositorio podrás encontrar mis avances y proyectos.

Actualmente, estoy explorando y construyendo proyectos enfocados en desarrollo web con Python y Reflex, con IA incorporada (análisis de datos, procesamiento del lenguaje natural, etc.).

Este portfolio es un reflejo de mi viaje profesional y de los nuevos conocimientos que estoy adquiriendo día a día. Como entusiasta del fitness y la tecnología, encuentro inspiración en la intersección entre ambos mundos.

Mi pasión por el desarrollo me lleva a buscar constantemente nuevas formas de crear soluciones innovadoras que realmente impacten en la vida de las personas."""
        },
        {
            "title": "Habilidades Técnicas",
            "content": """Mi stack tecnológico se centra en tecnologías modernas y versátiles:

🔧 Lenguajes y Frameworks:
• Python - Mi lenguaje principal para desarrollo web y backend
• Reflex 0.4 - Framework moderno para aplicaciones web con Python
• Angular - Desarrollo de interfaces de usuario dinámicas
• Symfony - Framework PHP para aplicaciones robustas

📊 Bases de Datos y Análisis:
• PostgreSQL - Base de datos relacional principal
• SQLModel - ORM moderno para Python
• Polars - Análisis de datos de alto rendimiento

🛠️ Herramientas de Desarrollo:
• Docker - Containerización y despliegue
• Figma - Diseño de interfaces y prototipado
• Postman - Testing y documentación de APIs
• Git/GitHub - Control de versiones y colaboración

🤖 Inteligencia Artificial:
• Procesamiento de lenguaje natural
• Análisis de datos con IA
• Integración de modelos de machine learning

Siempre en constante aprendizaje de las últimas tendencias tecnológicas."""
        },
        {
            "title": "Proyectos Destacados",
            "content": """Aquí puedes encontrar una muestra de los proyectos en los que he trabajado. Cada uno representa una oportunidad de aprendizaje y crecimiento:

🏢 Prácticas Finales de Grado - CodeArts Solutions ✅
Desarrollo del Frontend de un workspace colaborativo que combina funcionalidades de Trello y GitHub Projects. Trabajé en equipo para crear una solución integral de gestión de proyectos.
Tecnologías: Angular, Symfony, Docker, Figma, Postman, PostgreSQL

💪 TFG "Stronova" ✅
Mi Trabajo de Fin de Grado: una API revolucionaria para la gestión de entrenamientos en el ámbito fitness. Inspirado en mi experiencia personal como entusiasta del fitness, identifiqué la necesidad de una herramienta que integre y simplifique el seguimiento de entrenamientos, conectando eficientemente usuarios y entrenadores.
Tecnologías: Angular, Symfony, Docker, Figma, Postman, PostgreSQL
🔗 Proyecto disponible en GitHub: Stronova

🚧 PyBiz25 (En desarrollo)
ERP Inteligente con IA cuyo objetivo es centralizar documentación, inventario y procesos en una sola plataforma. Este proyecto representa la evolución hacia soluciones empresariales inteligentes.
Tecnologías: Python, Reflex 0.4, Polars, SQLModel, PostgreSQL"""
        },
        {
            "title": "Experiencia Profesional",
            "content": """Mi trayectoria profesional y académica:

🎓 Prácticas Finales de Grado - CodeArts Solutions
Como parte de mi formación académica, participé en el desarrollo de una plataforma colaborativa empresarial. Esta experiencia me permitió:
• Trabajar en un entorno profesional real con metodologías ágiles
• Desarrollar habilidades de trabajo en equipo y comunicación
• Aplicar conocimientos académicos en proyectos de impacto real
• Familiarizarme con herramientas de desarrollo empresarial

🚀 Proyectos Personales y Aprendizaje Continuo
Mi enfoque autodidacta me ha llevado a:
• Explorar tecnologías emergentes como Reflex para desarrollo web con Python
• Integrar IA en aplicaciones web prácticas
• Desarrollar soluciones que combinan mis intereses personales con necesidades reales del mercado
• Mantenerme actualizado con las últimas tendencias en desarrollo web y análisis de datos

💡 Filosofía de Trabajo
Creo firmemente en el aprendizaje continuo y en la importancia de crear soluciones que realmente aporten valor. Cada proyecto es una oportunidad para crecer profesionalmente y contribuir positivamente al ecosistema tecnológico."""
        },
        {
            "title": "Conectemos",
            "content": """¡Me encantaría conectar contigo! 🤝

Estoy siempre abierto a aprender, colaborar y recibir feedback. Si te interesa lo que hago, no dudes en contactarme.

📞 Información de Contacto:
• LinkedIn: jmgarciaaguera
• Email: josemanuelgarciaaguera@gmail.com
• GitHub: Puedes encontrar mis proyectos, incluyendo Stronova

💼 Oportunidades que me interesan:
• Desarrollo de aplicaciones web con Python y frameworks modernos
• Proyectos que integren IA y análisis de datos
• Colaboraciones en soluciones innovadoras para el sector fitness/wellness
• Oportunidades de desarrollo full-stack con tecnologías emergentes

🎯 ¿En qué puedo ayudarte?
• Desarrollo de APIs robustas y escalables
• Creación de interfaces de usuario modernas y responsivas
• Integración de soluciones de IA en aplicaciones web
• Consultoría en arquitectura de aplicaciones web

🌱 Siempre Aprendiendo
Mi objetivo es seguir creciendo profesionalmente, contribuir a proyectos significativos y formar parte de equipos que compartan la pasión por crear tecnología que marque la diferencia.

¡Espero que podamos trabajar juntos pronto!"""
        }
    ]
    
    @rx.var
    def total_pages(self) -> int:
        return len(self.pages)
    
    @rx.var
    def current_title(self) -> str:
        return self.pages[self.current_page]["title"]
    
    @rx.var
    def current_content(self) -> str:
        return self.pages[self.current_page]["content"]
    
    def next_page(self):
        if self.current_page < self.total_pages - 1:
            self.current_page += 1
    
    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1
    
    def go_to_page(self, page_num: int):
        if 0 <= page_num < self.total_pages:
            self.current_page = page_num