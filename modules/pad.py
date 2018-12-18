from pgzero.actor import Actor
from pgzero.keyboard import keyboard
from configs import *
import math

class Pad(Actor):

    def __init__(self, image='pad'):
        Actor.__init__(self, image=image)
        self.midbottom = math.ceil(WIDTH / 2), HEIGHT

    def update(self, dt):

        # 左右移动球板
        if keyboard.left:
            pad.x -= PAD_SPEED * dt
        if keyboard.right:
            pad.x += PAD_SPEED * dt

        # 限制移动范围
        if pad.right > WIDTH - BORDER:
            pad.right = WIDTH - BORDER
        if pad.left < BORDER:
            pad.left = BORDER

pad = Pad()

