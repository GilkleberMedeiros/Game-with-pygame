from pygame import *

# Arquivos carregados
PlayerIdle = image.load("Assets/Personagem.png")
Brick_Black = image.load("Assets/Brick_Black.png")
Brick_Light = image.load("Assets/Brick_Light.png")

FonteDefault = "./Roboto_Mono.zip"

rects = []    # Colission objects list
gameObjects = []   # General game objects list
uiObjects = []      # General ui objects
