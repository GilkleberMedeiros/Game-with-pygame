from pygame import *
from files import *

class Player():
    # '->' significa que a função retorna None
    def __init__(self, screen, x, y, width, heigth) -> None:
        self.screen = screen
        # dt para mover na velocidade dos frames por segundo
        self.dt = 0
        self.pos = [x, y, width, heigth]
        self.rect = self.screen.blit(Files.PlayerIdle, (self.pos[0], self.pos[1]))
        Files.rects.append(tuple(self.pos))

    def movement(self):
        clock = time.Clock()

        # Move the Player
        keys = key.get_pressed()
        if keys[K_LEFT] and self.colission(self.pos[0] - 30 * self.dt, "x"):
            self.pos[0] -= 30 * self.dt
        if keys[K_RIGHT] and self.colission(self.pos[0] + 30 * self.dt, "x"):
            self.pos[0] += 30 * self.dt
        if keys[K_DOWN] and self.colission(self.pos[1] + 30 * self.dt, "y"):
            self.pos[1] += 30 * self.dt
        if keys[K_UP] and self.colission(self.pos[1] + 30 * self.dt, "y"):
            self.pos[1] -= 30 * self.dt
        
        self.dt = clock.tick(60) / 1000

    def redraw(self):
        #draw.rect(self.screen, (100, 100, 100), tuple(self.rect))
        self.rect = self.screen.blit(Files.PlayerIdle, (self.pos[0], self.pos[1]))
    
    def colission(self, f_pos, pos: str):
        if pos.lower() == "x":
            self.rect[0] = f_pos
        elif pos.lower() == "y":
            self.rect[1] = f_pos
        
        print(Files.rects)
        if self.rect.collidelist(Files.rects) == -1:
            #print(Files.rects)
            return True
        return False
        

class Wall():
    def __init__(self, screen, x, y, width, heigth):
        self.screen = screen
        self.rect = [x, y, width, heigth]
        draw.rect(self.screen, (100, 100, 100), tuple(self.rect))

    def redraw(self):
        draw.rect(self.screen, (100, 100, 100), tuple(self.rect))

    
    