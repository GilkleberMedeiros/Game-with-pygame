import pygame
import player as p

pygame.init()
screen = pygame.display.set_mode(size=(810, 710))
clock = pygame.time.Clock()
running = True
player = p.Player(screen, 30, 30, 32, 32)
brick = p.Wall(screen, 150, 150, 32, 32)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    player.movement()
    screen.fill((0, 0, 0))
    player.redraw()
    brick.redraw()

    pygame.display.update()
    

    clock.tick(60)


pygame.quit()

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size=(810, 710))
        self.clock = pygame.time.Clock()
        self.player = p.Player(screen, 30, 30, 32, 32)
        self.running = True


if __name__ == "__main__":
    game = Game()
    game.loop()