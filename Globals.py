from pygame import *

# Imagens
PlayerIdle = image.load("Assets/Personagem.png")
Brick_Black = image.load("Assets/Brick_Black.png")
Brick_Light = image.load("Assets/Brick_Light.png")

# Fontes
DEFAULT_FONT = "./RobotoMono-VariableFont_wght.ttf"

rects = []    # Lista de colisão de objetos
gameObjects = []   # Lista de todos os objetos do jogo
uiObjects = []      # Lista dos objetos de interface

# Cores
WHITE = (255, 255, 255, 255)

# Mapas
MAP_PATH = "./map/mapa.tmx"

# Configurações de dos objetos do jogo
STANDARD_SIZE = 32

# Configurações de tela
