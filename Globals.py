from pygame import *
import msg_storage


# Imagens
PLAYER_IDLE = image.load("Assets/Sprites/Personagem.png")
BRICK_LIGHT = image.load("Assets/Sprites/Brick_Light.png")
BRICK_BLACK = image.load("Assets/Sprites/Brick_Black.png")

# Fontes
DEFAULT_FONT = "./Assets/Fonts/RobotoMono/RobotoMono-VariableFont_wght.ttf"

# Variáveis
dt = 0.0
screen = display.set_mode(size=(960, 640))
rects = []    # Lista de colisão de objetos
game_objects = []   # Lista de todos os objetos do jogo
ui_objects = []      # Lista dos objetos de interface

# Cores
WHITE = (255, 255, 255, 255)

# Mapas
MAP_PATH = "./Assets/Maps/map/mapa.tmx"

# Configurações de dos objetos do jogo
STANDARD_SIZE = 32

# Transferidor de dados
def get_data(name: str) -> any:
    if name.islower():
        try:
            return __file__.__getattribute__(name)
        except AttributeError:
            return None

def set_data(name: str, value: any) -> None:
    if name.islower():
        try:
            __file__.__setattr__(name, value)
        except AttributeError:
            pass

def append_data(name: str, value: any) -> None:
    if name.islower():
        try:
            lista = __file__.__getattribute__(name)
            lista.append(value)
            __file__.__setattr__(name, lista)
        except AttributeError:
            pass