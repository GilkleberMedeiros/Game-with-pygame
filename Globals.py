from pygame import *

# Constantes
# Imagens
PLAYER_IDLE = image.load("Assets/Sprites/Personagem.png")
BRICK_LIGHT = image.load("Assets/Sprites/Brick_Light.png")
BRICK_BLACK = image.load("Assets/Sprites/Brick_Black.png")
KEY_SPRITE = image.load("Assets/Sprites/Key.png")

# Sons
KEY_COLLECT_SONG = "Assets/Songs/Key_Collect_Song.wav"

# Fontes
DEFAULT_FONT = "./Assets/Fonts/RobotoMono/RobotoMono-VariableFont_wght.ttf"

# Tela
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 640
SCREEN = display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))

# Cores
WHITE = (255, 255, 255, 255)

# Mapas
MAP_PATH = "./Assets/Maps/map/mapa.tmx"

# Configurações de dos objetos do jogo
STANDARD_SIZE = 32


data = {"collissors": [], "screen_objects": [], "dt": 0.0}

# Transferidor de dados
def get_data(name: str) -> any:
    try:
        return data[name]
    except:
        return None

def set_data(name: str, value: any) -> None:
    try:
        data[name] = value
    except:
        return None

def append_data(name: str, value: any) -> None:
    try:
        data[name].append(value)
    except:
        return None
    

# Sistema de mensagens
msgs = {"stop": False, "instance": None}

def get_msg(key):
    return msgs[key]

def set_msg(key, value):
    msgs[key] = value