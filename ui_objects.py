from Globals import *
from typing import Callable


class Button(font.Font):
    def __init__(self, 
                 font: str, 
                 size: float, 
                 action: Callable, 
                 *args: tuple,
                 key: int=K_SPACE):
        super().__init__(font, size)
        self.screen = SCREEN
        self.__action = action
        self.__key = key
        self.__args = args
        append_data("screen_objects", self)
    
    def do_on_mainloop(self) -> None:
        self.listen()
        self.redraw()

    def set_surface(self, text: str, antialias: bool=True, color: tuple=WHITE) -> None:
        self.surface = self.render(text, antialias, color)

    def redraw(self, pos: tuple=None) -> None:
        if pos is None:
            pos = self.__pos
        else:
            self.__pos = pos

        self.screen.blit(self.surface, pos)

    def listen(self):
        keys = key.get_pressed()
        if keys[self.__key]:
            if self.__args:
                self.__action(self.__args)
            else:
                self.__action()
        

class Label(font.Font):
    def __init__(self, 
                 font, 
                 size: float):
        super().__init__(font, size)
        self.screen = SCREEN
        append_data("screen_objects", self)

    def do_on_mainloop(self) -> None:
        self.redraw()

    def set_surface(self, text: str, antialias: bool=True, color: tuple=WHITE) -> None:
        self.surface = self.render(text, antialias, color)

    def redraw(self, pos: tuple=None) -> None:
        if pos is None:
            pos = self.__pos
        else:
            self.__pos = pos
        
        self.screen.blit(self.surface, pos)


# Compotamento dos botões
def play_button_behavior(screen_content: tuple[object]):
    set_msg("instance", screen_content[0])

def quit_button_behavior():
    set_msg("stop", True)