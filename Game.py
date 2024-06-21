from player import *
from pytmx import TiledMap
from uiObjects import Label


# Helpers
dt = 0.0
screen = display.set_mode(size=(960, 640))

# Configs
objSize = 32
TileMap = TiledMap("./map/mapa.tmx")
white = Color(255, 255, 255, 255)

class Init_screen:
    def __init__(self):

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
        screen.fill((0, 0, 0))
        screen.blit(self.title, (screen.get_width() // 2, 20))
        screen.blit(self.jogar, (screen.get_width() // 2, 450))
        screen.blit(self.op, (screen.get_width() // 2, 500))
        screen.blit(self.quit, (screen.get_width() // 2, 550))

        display.update()


class Game():
    def __init__(self):
        for layer in TileMap.layers:
            for obj in layer:
                if obj[2] == 1:
                    Wall(screen, obj[0] * objSize, obj[1] * objSize, objSize, objSize)
                else:
                    Floor(screen, obj[0] * objSize, obj[1] * objSize, objSize, objSize)

        self.player = Player(screen, 32, 32, objSize, objSize)

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