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

ball = Ball(100, 50)



def draw():
    screen.clear()
    ball.draw_ball()

def update(dt):
    uy = ball.vy
    ball.vy = ball.vy + GRAVITY * dt
    ball.y = ball.y + (uy + ball.vy) * 0.5 * dt
    



pgzrun.go()