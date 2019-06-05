import pgzrun
import math
import random
from configs import *
from modules.pad import *
from modules.ball import *
from modules.block import *

# 计算方块矩阵的左上角坐标
LEFT = (WIDTH - BLOCKS_PER_GROUP * BLOCK_WIDTH) / 2
TOP = (BORDER + BLOCK_HEIGHT)

# 生成方块矩阵
blocks = []
for g in range(0, BLOCK_GROUPS):
    for i in range(0, BLOCKS_PER_GROUP):
        block = Block()
        block.left = LEFT + i * BLOCK_WIDTH
        block.top = TOP + g * BLOCK_HEIGHT
        blocks.append(block)

def update(dt):

    # 更新球和球拍的位置
    pad.update(dt)
    ball.update(dt)

    # 检查球和边缘的碰撞
    ball.check_with_border()

    # 检查和球拍的碰撞
    ball.check_with_rect(pad)

    # 检查和方块的碰撞
    for i, block in enumerate(blocks):
        if ball.check_with_rect(block):

            # 销毁已破坏的方块
            if block.isBroken:
                del blocks[i]

            # 破坏完好的方块
            else:
                block.broken()

def draw():
    screen.clear()
    screen.blit('border', (0,0))
    pad.draw()
    ball.draw()
    for block in blocks:
        block.draw()

def on_key_down(key):
    if key == keys.ESCAPE:
        exit()

pgzrun.go()
