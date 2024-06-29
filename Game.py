from player import *
from pytmx import TiledMap
from ui_objects import *


def main():
    init()
    mainloop(Init_Screen)
    quit()

def mainloop(content):
    running = True
    clock = time.Clock()
    content_to_load = content()

    while running:
        instance_msg = msg_storage.get_msg("instance")
        stop_msg = msg_storage.get_msg("stop")

        for e in event.get():
            if e.type == QUIT:
                running = False
            elif instance_msg is not None:
                content_to_load = instance_msg()
                msg_storage.set_msg("instance", None)
            elif stop_msg:
                running = False

        update()
        dt = clock.tick(60) / 1000
        set_data("dt", dt)

def update():
        SCREEN.fill((0, 0, 0))
        objects = get_data("screen_objects")

        for obj in objects:
            obj.do_on_mainloop()
        
        display.update()

class Init_Screen:
    def __init__(self):
        # Title label
        self.title = Label(DEFAULT_FONT, 20)
        self.title.set_surface("Labirinto dos passáros")
        self.title.redraw((348, 20))

        # Play Button
        self.play_button = Button(DEFAULT_FONT, 16, play_button_behavior, Game, key=K_SPACE)
        self.play_button.set_surface("Jogar: Espaço")
        self.play_button.redraw((415, 440))

        # Quit Button
        self.quit_button = Button(DEFAULT_FONT, 16, quit_button_behavior, key=K_q)
        self.quit_button.set_surface("Sair: Q")
        self.quit_button.redraw((445, 490))


class Game():
    def __init__(self):
        TileMap = TiledMap(MAP_PATH)
        for layer in TileMap.layers:
            for obj in layer:
                if obj[2] == 1:
                    Wall(obj[0] * STANDARD_SIZE, obj[1] * STANDARD_SIZE, STANDARD_SIZE, STANDARD_SIZE)
                else:
                    Floor(obj[0] * STANDARD_SIZE, obj[1] * STANDARD_SIZE, STANDARD_SIZE, STANDARD_SIZE)

        self.player = Player(32, 32, STANDARD_SIZE, STANDARD_SIZE)
        

class End_Screen():
    def __init__(self):
        # Thanks Label
        self.thanks = Label(DEFAULT_FONT, 20)
        self.thanks.set_surface("Obrigado por jogar!!!")
        self.thanks_pos = self.thanks.size("Obrigado por jogar!!!")
        self.thanks_pos = ((SCREEN_WIDTH // 2) - (self.thanks_pos[0] // 2), 20)
        self.thanks.redraw(self.thanks_pos)

        # Quit Button
        self.quit_button = Button(DEFAULT_FONT, 16, quit_button_behavior, key=K_q)
        self.quit_button.set_surface("Sair: Q")
        self.quit_button_pos = self.quit_button.size("Sair: Q")
        self.quit_button_pos = ((SCREEN_WIDTH // 2) - (self.quit_button_pos[0] // 2), 440)
        self.quit_button.redraw(self.quit_button_pos)


if __name__ == "__main__":
    main()