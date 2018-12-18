from pgzero.actor import Actor
from . import helpers
from .pad import *
from configs import *
import math
import random

class Ball(Actor):

    def __init__(self, image='ball'):    
        Actor.__init__(self, image=image)
        self.midbottom = math.ceil(WIDTH / 2), HEIGHT - pad.height
        self.speedX = random.uniform(- BALL_INIT_SPEED, BALL_INIT_SPEED)
        self.speedY = - BALL_INIT_SPEED
        self.radius = self.width / 2

    def update(self, dt):

        # 移动球
        self.x += self.speedX * dt
        self.y += self.speedY * dt

    def check_with_border(self):

        if self.top <= BORDER:
            self.bounce_top(BORDER)

        if self.left <= BORDER:
            self.bounce_left(BORDER)

        if self.right >= WIDTH - BORDER:
            self.bounce_right(WIDTH - BORDER)

    def check_with_rect(self, rect):

        # 先做简单的矩形检测
        if not self.colliderect(rect):
            return False

        # 计算最近点距离
        pX = helpers.clamp(self.x, rect.left, rect.right)
        pY = helpers.clamp(self.y, rect.top, rect.bottom)
        distance = helpers.distance(self.x, self.y, pX, pY)

        # 距离不够，未碰撞
        if distance > self.radius:
            return False

        # 碰在角上，按碰撞角度反弹
        if pX in (rect.left, rect.right) and pY in (rect.top, rect.bottom):

            ratio = abs(self.x - pX) / abs(self.y - pY)

            speedY = math.sqrt(math.pow(self.speed, 2) / (math.pow(ratio, 2) + 1))
            speedX = speedY * ratio

            self.speedX = speedX if self.x > pX else - speedX
            self.speedY = speedY if self.y > pY else - speedY

        # 碰在边上，直接反弹
        elif pX == rect.left:
            self.bounce_right(rect.left)
        elif pX == rect.right:
            self.bounce_left(rect.right)
        elif pY == rect.top:
            self.bounce_bottom(rect.top)
        elif pY == rect.bottom:
            self.bounce_top(rect.bottom)

        return True

    def bounce_top(self, top):
        self.top = top
        self.speedY = -self.speedY

    def bounce_bottom(self, bottom):
        self.bottom = bottom
        self.speedY = -self.speedY

    def bounce_left(self, left):
        self.left = left
        self.speedX = -self.speedX

    def bounce_right(self, right):
        self.right = right
        self.speedX = -self.speedX

    @property
    def speed(self):
        return math.sqrt(math.pow(self.speedX, 2) + math.pow(self.speedY, 2))
    
ball = Ball()
