from pygame import *
from player import *


# Helpers
dt = 0.0
screen = display.set_mode(size=(810, 710))

# Configs
objSize = 32

class Game():
    def __init__(self):
        init()
        self.player = Player(screen, 30, 30, objSize, objSize)

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
    game = Game()
    game.loop()
    quit()