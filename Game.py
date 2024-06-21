from player import *
from pytmx import TiledMap
from uiObjects import Label


# Helpers
dt = 0.0
screen = display.set_mode(size=(960, 640))


TileMap = TiledMap(MAP_PATH)

class Init_screen:
    def __init__(self):
        self.title = Label(DEFAULT_FONT, 20, screen)
        self.title.set_text("Labirinto dos passáros")
        self.title.draw_text((348, 0))

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