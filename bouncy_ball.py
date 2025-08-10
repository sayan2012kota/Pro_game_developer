import pgzrun
TITLE = "Bouncy Ball"

WIDTH = 500
HEIGHT = 800

GRAVITY = 2000

class Ball():
    def __init__(self, x, y, radius, colour):
        self.x = x
        self.y = y
        self.vx = 200
        self.vy = 0
        self.radius = radius
        self.colour = colour


    def draw_ball(self):
        screen.draw.filled_circle((self.x, self.y), self.radius, self.colour)


ball = Ball(100, 50, 25, "blue")
ball_2 = Ball(300, 50, 50, "red")


def draw():
    screen.clear()
    ball.draw_ball()
    #ball_2.draw_ball()

def update(dt):
    uy = ball.vy
    ball.vy = ball.vy + GRAVITY * dt
    ball.y = ball.y + (uy + ball.vy) * 0.5 * dt

    ball.x = ball.x + ball.vx * dt
    if ball.x >= WIDTH or ball.x <= 0:
        ball.vx = -ball.vx
    if ball.y >= HEIGHT:
        ball.y = HEIGHT - ball.radius
        ball.vy = -ball.vy * 0.9


pgzrun.go()