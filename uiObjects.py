from Globals import *

class Button(font.Font):
    def __init__(self, font, size, text, ):
        super().__init__(font, size)
        self.text = text
    
    def get_surface(self, screen):
        pass

class Label(font.Font):
    def __init__(self, 
                 font, 
                 size: float, 
                 screen: Surface):
        super().__init__(font, size)
        self.screen = screen

    def set_text(self, text: str, antialias: bool=True, color: tuple=WHITE) -> None:
        self.surface = self.render(text, antialias, color)

    def draw_text(self, pos: tuple) -> None:
        self.screen.blit(self.surface, pos)


