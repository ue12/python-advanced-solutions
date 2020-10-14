import pygame as pg
from itertools import product
from random import choice

BOARD = (20, 20)
CELL_SIZE = 30
SCREEN_SIZE = tuple(x * CELL_SIZE for x in BOARD)

pg.init()
screen = pg.display.set_mode(SCREEN_SIZE)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# les coordonnées du corps du serpent
serpent = [
    (10, 15),
    (11, 15),
    (12, 15),
]
direction = (1, 0)

# le score
score = 0
pg.display.set_caption(f"Score: {score}")

def ajout_vecteurs(x, y):
    return (x[0]+y[0], x[1]+y[1])

def est_sorti(x):
    return x[0] < 0 or x[0] >= BOARD[0] or x[1] < 0 or x[1] >= BOARD[1]

def placer_fruit():
    num_lignes, num_col = BOARD
    positions = list(product(range(num_lignes), range(num_col)))
    positions_libres = [pos for pos in positions if pos not in serpent]
    return choice(positions_libres)

fruit = placer_fruit()

running = True
clock = pg.time.Clock()
while running:
    clock.tick(3)

    # 1. lecture des évênements
    new_direction = direction
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                running = False
            elif event.key == pg.K_UP:
                if direction != (0, 1):
                    new_direction = (0, -1)
            elif event.key == pg.K_DOWN:
                if direction != (0, -1):
                    new_direction = (0, 1)
            elif event.key == pg.K_RIGHT:
                if direction != (-1, 0):
                    new_direction = (1, 0)
            elif event.key == pg.K_LEFT:
                if direction != (1, 0):
                    new_direction = (-1, 0)
    direction = new_direction

    # 2. actions
    # 2.a on déplace le serpent
    new_head = ajout_vecteurs(serpent[-1], direction)
    queue = serpent[0]
    serpent = [*serpent[1:], new_head]
    # et on vérifie que le déplacement est valide
    if est_sorti(new_head):
        print("PERDU: VOUS ÊTES SORTI !")
        running = False
    if new_head in serpent[:-1]:
        # le serpent se mord la queue
        print("PERDU: LE SERPENT S'EST MORDU LA QUEUE !")
        running = False
    # 2.b le serpent mange le fruit
    if new_head == fruit:
        serpent = [queue, *serpent]
        fruit = placer_fruit()
        score += 1
        pg.display.set_caption(f"Score: {score}")

    # 3. rendu
    screen.fill(WHITE)
    rect = pg.Rect(fruit[0] * CELL_SIZE, fruit[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pg.draw.rect(screen, RED, rect)
    for x, y in serpent:
        rect = pg.Rect(x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pg.draw.rect(screen, BLACK, rect)

    pg.display.update()

print(f"SCORE FINAL {score}")
pg.quit()
