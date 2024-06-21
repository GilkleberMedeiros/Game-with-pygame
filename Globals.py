from pygame import *

# Imagens
PlayerIdle = image.load("Assets/Sprites/Personagem.png")
Brick_Black = image.load("Assets/Sprites/Brick_Black.png")
Brick_Light = image.load("Assets/Sprites/Brick_Light.png")

# Fontes
DEFAULT_FONT = "./Assets/Fonts/RobotoMono/RobotoMono-VariableFont_wght.ttf"

rects = []    # Lista de colisão de objetos
gameObjects = []   # Lista de todos os objetos do jogo
uiObjects = []      # Lista dos objetos de interface

# Cores
WHITE = (255, 255, 255, 255)

# Mapas
MAP_PATH = "./Assets/Maps/map/mapa.tmx"

# Configurações de dos objetos do jogo
STANDARD_SIZE = 32

# Configurações de tela
