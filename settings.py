WIDTH = 700
HEIGHT = 700
PLAYER_ACC = 2
PLAYER_FRICTION = -0.3
PLAYER_JUMP = 15
PLAYER_GRAV = 0.8
GAME_FONT = 'inkfree'
FPS = 60

# define colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
BABYBLUE = (137, 207, 240)
SLIME = (50, 205, 50)
RED = (255,50,50)
GOLD = (255, 215, 0)

# defines a random color
from random import randint
RANDCOLOR = [randint(0,255), randint(0,255), randint(0,255)]

# Starting platforms
PLATFORMS_LIST = (WIDTH / 2 -50, HEIGHT/2, 100, 20, (BABYBLUE), "normal"),
                