import pygame as pg
from random import randint

W, H = 20, 20
X, Y = 30, 30
BACKGROUND_COLOR = (255, 255, 255)
SNAKE_COLOR = (0, 0, 0)

pg.init()
screen = pg.display.set_mode((X*W, Y*H))
clock = pg.time.Clock()


def draw_snake(snake):
    screen.fill(BACKGROUND_COLOR)
    for (x, y) in snake:
        rect = pg.Rect(x*W, y*H, W, H)
        pg.draw.rect(screen, SNAKE_COLOR, rect)

# on rajoute une condition à la boucle: si on la passe à False le programme s'arrête

snake = [
    (10, 15),
    (11, 15),
    (12, 15),
]

running = True
while running:

    draw_snake(snake)
    pg.display.update()

    # on itère sur tous les évênements qui ont eu lieu depuis le précédent appel
    # ici donc tous les évènements survenus durant la seconde précédente
    for event in pg.event.get():
        # chaque évênement à un type qui décrit la nature de l'évênement
        # un type de pg.QUIT signifie que l'on a cliqué sur la "croix" de la fenêtre
        if event.type == pg.QUIT:
            running = False
        # un type de pg.KEYDOWN signifie que l'on a appuyé une touche du clavier
        elif event.type == pg.KEYDOWN:
            # si la touche est "Q" on veut quitter le programme
            if event.key == pg.K_q:
                running = False

    clock.tick(1)

# Enfin on rajoute un appel à pg.quit()
# Cet appel va permettre à Pygame de "bien s'éteindre" et éviter des bugs sous Windows
pg.quit()
