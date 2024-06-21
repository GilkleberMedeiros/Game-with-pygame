from player import *
from pytmx import TiledMap
from uiObjects import Label, Button


# Helpers
dt = 0.0
screen = display.set_mode(size=(960, 640))


TileMap = TiledMap(MAP_PATH)

class Init_screen:
    def __init__(self):
        # Title label
        self.title = Label(DEFAULT_FONT, 20, screen)
        self.title.set_surface("Labirinto dos passáros")
        self.title.redraw((348, 0))

        # Play Button
        self.play_button = Button(DEFAULT_FONT, 16, screen, lambda df: print(1 + 1))
        self.play_button.set_surface("Jogar: Espaço")
        self.play_button.redraw((415, 440))
        print(self.play_button.size("Jogar: Espaço"))

        # Quit Button
        self.quit_button = Button(DEFAULT_FONT, 16, screen, lambda df: print(1 + 1))
        self.quit_button.set_surface("Sair: Q")
        self.quit_button.redraw((445, 490))
        print(self.quit_button.size("Sair: Q"))

        uiObjects.append(self.title)
        uiObjects.append(self.play_button)
        uiObjects.append(self.quit_button)

        self.loop()
    
    def loop(self):
        global dt
        running = True
        clock = time.Clock()
        while running:
            for e in event.get():
                if e.type == QUIT:
                    running = False

            self.update()
            dt = clock.tick(60) / 1000
    
    def update(self):
        global screen
        for obj in gameObjects:
            if isinstance(obj, Button):
                obj.listen()
            obj.redraw()

        display.update()


class Game():
    def __init__(self):
        for layer in TileMap.layers:
            for obj in layer:
                if obj[2] == 1:
                    Wall(screen, obj[0] * STANDARD_SIZE, obj[1] * STANDARD_SIZE, STANDARD_SIZE, STANDARD_SIZE)
                else:
                    Floor(screen, obj[0] * STANDARD_SIZE, obj[1] * STANDARD_SIZE, STANDARD_SIZE, STANDARD_SIZE)

        self.player = Player(screen, 32, 32, STANDARD_SIZE, STANDARD_SIZE)

    def loop(self):
        global dt
        running = True
        clock = time.Clock()
        while running:
            for e in event.get():
                if e.type == QUIT:
                    running = False

            self.update()
            dt = clock.tick(60) / 1000
        
    def update(self):
        global screen
        self.player.movement(dt)
        screen.fill((0, 0, 0))

        for obj in gameObjects:
            obj.redraw()
        
        display.update()


if __name__ == "__main__":
    init()
    Init_screen()
    quit()