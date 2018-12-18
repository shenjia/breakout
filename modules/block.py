from pgzero.actor import Actor
from . import helpers
from configs import *

class Block(Actor):

    isBroken = False

    def __init__(self, image='block', x = 0, y = 0):    
        Actor.__init__(self, image=image)
        self.center = WIDTH / 2, HEIGHT / 2

    def broken(self):

        self.image = 'block_broken'
        self.isBroken = True