import pgzrun
TITLE = "Bouncy Ball"

WIDTH = 500
HEIGHT = 800

colour = "blue"

GRAVITY = 2000

class Ball():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 200
        self.vy = 0
        self.radius = 25

    def draw_ball(self):
        screen.draw.filled_circle((self.x, self.y), self.radius, colour)

ball = Ball(0, 800)

def draw():
    ball.draw_ball()

def update():
    pass
    



pgzrun.go()