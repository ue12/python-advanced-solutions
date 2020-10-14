import pygame as pg
from random import randint

W, H = 20, 20
X, Y = 30, 30
BACKGROUND_COLOR = (255, 255, 255)
SNAKE_COLOR = (0, 0, 0)
FRUIT_COLOR = (255, 0, 0)

DIRECTIONS = {
    'DOWN': (0, 1),
    'UP': (0, -1),
    'RIGHT': (1, 0),
    'LEFT': (-1, 0),
}

DIRECTION = DIRECTIONS['RIGHT']

snake = [
    (10, 15),
    (11, 15),
    (12, 15),
]

FRUIT = (10, 10)


pg.init()
screen = pg.display.set_mode((X*W, Y*H))
clock = pg.time.Clock()
pg.display.set_caption(f"Score: {len(snake)}")


def draw_game(snake, fruit):
    screen.fill(BACKGROUND_COLOR)
    for (x, y) in snake:
        rect = pg.Rect(x*W, y*H, W, H)
        pg.draw.rect(screen, SNAKE_COLOR, rect)
    x, y = fruit
    rect = pg.Rect(x*W, y*H, W, H)
    pg.draw.rect(screen, FRUIT_COLOR, rect)
    pg.display.update()

def in_scope(point):
    x, y = point
    return 0 <= x < X and 0 <= y < Y

def quit(snake, reason):
    print(f"Game over ({reason}) with a score of {len(snake)}")
    pg.quit()
    exit()

def move_snake(snake, direction):
    global FRUIT
    # the new first piece is based on the current first piece
    head = snake[-1]
    # compute it
    x, y = head
    dx, dy = direction
    new_head = (x+dx , y+dy)
    if new_head == FRUIT:
        snake.append(FRUIT)
        FRUIT = (randint(0, X), randint(0, Y))
        pg.display.set_caption(f"Score: {len(snake)}")
    elif new_head in snake:
        quit(snake, "self-bite")
    elif not in_scope(new_head):
        quit(snake, "out-of-board")
    else:
        # the last item in snake just vanishes
        _tail = snake.pop(0)
        # insert as the new head
        snake.append(new_head)

running = True
while running:

    draw_game(snake, FRUIT)


    # on itère sur tous les évênements qui ont eu lieu depuis le précédent appel
    # ici donc tous les évènements survenus durant la seconde précédente
    for event in pg.event.get():
        #print(f"{event=}")
        # chaque évênement à un type qui décrit la nature de l'évênement
        # un type de pg.QUIT signifie que l'on a cliqué sur la "croix" de la fenêtre
        if event.type == pg.QUIT:
            running = False
        # un type de pg.KEYDOWN signifie que l'on a appuyé une touche du clavier
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_DOWN:
                DIRECTION = DIRECTIONS['DOWN']
            elif event.key == pg.K_UP:
                DIRECTION = DIRECTIONS['UP']
            elif event.key == pg.K_RIGHT:
                DIRECTION = DIRECTIONS['RIGHT']
            elif event.key == pg.K_LEFT:
                DIRECTION = DIRECTIONS['LEFT']
            # si la touche est "Q" on veut quitter le programme
            elif event.key == pg.K_q:
                running = False
    move_snake(snake, DIRECTION)

    clock.tick(4)

# Enfin on rajoute un appel à pg.quit()
# Cet appel va permettre à Pygame de "bien s'éteindre" et éviter des bugs sous Windows
pg.quit()
