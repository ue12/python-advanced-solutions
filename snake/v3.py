import pygame as pg
from random import randint

# in pixels
W, H = 20, 20
# in snake units
X, Y = 30, 30

BACKGROUND_COLOR = (255, 255, 255)
SNAKE_COLOR = (0, 0, 0)

pg.init()
screen = pg.display.set_mode((X*W, Y*H))
clock = pg.time.Clock()

# on rajoute une condition à la boucle: si on la passe à False le programme s'arrête
running = True
while running:

    random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    screen.fill(BACKGROUND_COLOR)

    for x in range(X):
        for y in range(Y):
            if (x+y) % 2 == 0:
                xp = x*W # coordonnée x (colonnes) en pixels
                yp = y*H # coordonnée y (lignes) en pixels
                rect = pg.Rect(xp, yp, W, H)
                pg.draw.rect(screen, SNAKE_COLOR, rect)

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
