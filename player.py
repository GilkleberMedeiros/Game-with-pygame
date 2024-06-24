from Globals import *


class Player():
    # '->' significa que a função retorna None
    def __init__(self, screen, x, y, width, heigth) -> None:
        self.screen = screen
        self.pos = [x, y, width, heigth]
        self.rect = screen.blit(PLAYER_IDLE, Rect(self.pos))
        rects.append((self.rect, self.__class__))
        game_objects.append(self)

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

        # Corners of player rect
        corners = [[self.rect[0], self.rect[1]], # :left upper
                  [self.rect[0] + self.rect[2] - 1, self.rect[1]], # :right upper 
                  [self.rect[0], self.rect[1] + self.rect[3] - 1], # :left lower
                  [self.rect[0] + self.rect[2] - 1, self.rect[1] + self.rect[3] - 1]] # :right lower
        for i in rects:
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
        self.screen.blit(BRICK_BLACK, (self.rect[0], self.rect[1]))
        rects.append((self.rect, self.__class__))
        game_objects.append(self)

    def do_on_mainloop(self) -> None:
        self.redraw()

    def redraw(self):
        self.screen.blit(BRICK_BLACK, (self.rect[0], self.rect[1]))


class Floor():
    def __init__(self, screen, x, y, width, heigth):
        self.screen = screen
        self.rect = [x, y, width, heigth]
        self.screen.blit(BRICK_LIGHT, Rect(self.rect))
        game_objects.append(self)

    def do_on_mainloop(self) -> None:
        self.redraw()

    def redraw(self):
        self.screen.blit(BRICK_LIGHT, Rect(self.rect))

