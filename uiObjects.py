from Globals import *
from typing import Callable

class Button(font.Font):
    def __init__(self, 
                 font, 
                 size: float, 
                 screen: Surface,
                 action: Callable, 
                 key: int=K_SPACE, 
                 *args):
        super().__init__(font, size)
        self.screen = screen
        self.__action = action
        self.__key = key
        self.__args = args

    def set_surface(self, text: str, antialias: bool=True, color: tuple=WHITE) -> None:
        self.surface = self.render(text, antialias, color)

    def redraw(self, pos: tuple) -> None:
        self.screen.blit(self.surface, pos)

    def listen(self):
        keys = key.get_pressed()
        if keys[self.__key]:
            self.__action(self.__args)
        

class Label(font.Font):
    def __init__(self, 
                 font, 
                 size: float, 
                 screen: Surface):
        super().__init__(font, size)
        self.screen = screen

    def set_surface(self, text: str, antialias: bool=True, color: tuple=WHITE) -> None:
        self.surface = self.render(text, antialias, color)

    def redraw(self, pos: tuple) -> None:
        self.screen.blit(self.surface, pos)


class CollumButtons:
    def __init__(self, 
                 screen: Surface, 
                 area: Rect, 
                 buttons: list[Button], 
                 gap: int=5):
        self.screen = screen
        self.__area = area
        self.__buttons = buttons
        self.__collum_buttons = Surface(area[2], area[3])
        self.__gap = gap
        self.__selected_button = 0
        self.__pos_buttons()
    
    def __pos_buttons(self):
        for y in range(self.__area[1], self.__area[3], self.__gap):
            button = next(iter(self.__buttons))
            x = (self.__area[2] // 2) - (button.surface.get_width() // 2)
            self.__collum_buttons.blit(button.surface, (x, y))

    def listen(self):
        keys = key.get_pressed()

    def redraw(self):
        self.screen.blit(self.__collum_buttons, self.area[0:2])

