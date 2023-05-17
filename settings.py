WIDTH = 700
HEIGHT = 700
PLAYER_ACC = 2
PLAYER_FRICTION = -0.3
PLAYER_JUMP = 20
PLAYER_GRAV = 0.8
MOB_ACC = 2
MOB_FRICTION = -0.3
GAME_FONT = 'arial'

# define colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
BABYBLUE = (137, 207, 240)
SLIME = (50, 205, 50)
RED = (255,50,50)

# defines a random color
from random import randint
RANDCOLOR = [randint(0,255), randint(0,255), randint(0,255)]
RANDCOLOR2 = [randint(0,255), randint(0,255), randint(0,255)]

FPS = 60
RUNNING = True
SCORE = 0
PAUSED = False

# Starting platforms
PLATFORMS_LIST = [(0, HEIGHT - 40, WIDTH, 40, (200,200,200), "normal"),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20, (SLIME), "bouncey"),
                #  (500, HEIGHT - 300, 100, 5, (200,200,200), "disappearing "),
                 (350, 200, 100, 20, (BABYBLUE), "normal"),
                 (175, 400, 100, 20, (BABYBLUE), "normal")]