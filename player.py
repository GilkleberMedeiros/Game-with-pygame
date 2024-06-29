from Globals import *


class Player():
    # '->' significa que a função retorna None
    def __init__(self, x, y, width, heigth) -> None:
        self.screen = SCREEN
        self.pos = [x, y, width, heigth]
        self.rect = self.screen.blit(PLAYER_IDLE, Rect(self.pos))
        append_data("collissors", (self.rect, self.__class__))
        append_data("screen_objects", self)

    def do_on_mainloop(self) -> None:
        self.movement()
        self.redraw()

    def movement(self) -> None:
        dt = get_data("dt")
        
        keys = key.get_pressed()
        if keys[K_LEFT] and self.colission((self.pos[0] / 1) - 1, "x"):
            self.pos[0] -= 30 * dt
        if keys[K_RIGHT] and self.colission((self.pos[0] / 1) + 1, "x"):
            self.pos[0] += 30 * dt
        if keys[K_DOWN] and self.colission((self.pos[1] / 1) + 1, "y"):
            self.pos[1] += 30 * dt
        if keys[K_UP] and self.colission((self.pos[1] / 1) - 1, "y"):
            self.pos[1] -= 30 * dt

    def redraw(self) -> None:
        self.rect = self.screen.blit(PLAYER_IDLE, Rect(self.pos))
    
    def colission(self, f_pos: float | int, direc: str) -> bool:
        """
        Check if player is colliding with another game object from
        Files.rects
        param: float | int, str
        return: bool
        """
        if direc.lower() == "x":
            self.rect[0] = f_pos
        elif direc.lower() == "y":
            self.rect[1] = f_pos

        collissors = get_data("collissors")

        # Corners of player rect
        corners = [[self.rect[0], self.rect[1]], # :left upper
                  [self.rect[0] + self.rect[2] - 1, self.rect[1]], # :right upper 
                  [self.rect[0], self.rect[1] + self.rect[3] - 1], # :left lower
                  [self.rect[0] + self.rect[2] - 1, self.rect[1] + self.rect[3] - 1]] # :right lower
        for i in collissors:
            if i[1] == Player:
                continue

            # xy1 True if left upper corner inside of another rect
            xy1 = (corners[0][0] <= (i[0][0] + i[0][2] - 1) and \
                   corners[0][0] >= i[0][0]) and \
                  (corners[0][1] <= (i[0][1] + i[0][3] - 1) and \
                   corners[0][1] >= i[0][1])
            # xy2 True if right upper corner inside of another rect
            xy2 = (corners[1][0] <= (i[0][0] + i[0][2] - 1) and \
                   corners[1][0] >= i[0][0]) and \
                  (corners[1][1] <= (i[0][1] + i[0][3] - 1) and \
                   corners[1][1] >= i[0][1])
            # xy3 True if left lower corner inside of another rect
            xy3 = (corners[2][0] <= (i[0][0] + i[0][2] - 1) and \
                   corners[2][0] >= i[0][0]) and \
                  (corners[2][1] <= (i[0][1] + i[0][3] - 1) and \
                   corners[2][1] >= i[0][1])
            # xy4 True if right lower corner inside of another rect
            xy4 = (corners[3][0] <= (i[0][0] + i[0][2] - 1) and \
                   corners[3][0] >= i[0][0]) and \
                  (corners[3][1] <= (i[0][1] + i[0][3] - 1) and \
                   corners[3][1] >= i[0][1])
            
            if xy1 or xy2 or xy3 or xy4:
                return False
        return True
    

class Wall():
    def __init__(self, x, y, width, heigth):
        self.screen = SCREEN
        self.rect = [x, y, width, heigth]
        self.screen.blit(BRICK_BLACK, (self.rect[0], self.rect[1]))
        append_data("collissors", (self.rect, self.__class__))
        append_data("screen_objects", self)

    def do_on_mainloop(self) -> None:
        self.redraw()

    def redraw(self):
        self.screen.blit(BRICK_BLACK, (self.rect[0], self.rect[1]))


class Floor():
    def __init__(self, x, y, width, heigth):
        self.screen = SCREEN
        self.rect = [x, y, width, heigth]
        self.screen.blit(BRICK_LIGHT, Rect(self.rect))
        append_data("screen_objects", self)

    def do_on_mainloop(self) -> None:
        self.redraw()

    def redraw(self):
        self.screen.blit(BRICK_LIGHT, Rect(self.rect))

