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
        Files.rects.append(self.rect)

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
        self.rect = self.screen.blit(Files.PlayerIdle, (self.pos[0], self.pos[1]))
    
    def colission(self, f_pos, direc: str):
        if direc.lower() == "x":
            self.rect[0] = f_pos
        elif direc.lower() == "y":
            self.rect[1] = f_pos
        
        colission_list = self.get_colission_list(self.rect, Files.rects)
        return self.rect.collidelist(colission_list) == -1
    
    def get_colission_list(self, rect: Rect, colission_list: list) -> list:
        """
            Remove a rect if is in a colission list
            with +1 and -1 tolerance
            param: rect, list
            return: list
        """
        return_list = colission_list.copy()
        for i in return_list:
            count = 0
            for j in i:
                if j < rect[count] - 1 and j > rect[count] + 1:
                    break
                count += 1
            else:
                return_list.remove(i)

        return return_list


        

class Wall():
    def __init__(self, screen, x, y, width, heigth):
        self.screen = screen
        self.rect = [x, y, width, heigth]
        draw.rect(self.screen, (100, 100, 100), tuple(self.rect))
        Files.rects.append(Rect(self.rect))

    def redraw(self):
        draw.rect(self.screen, (100, 100, 100), tuple(self.rect))

    
    