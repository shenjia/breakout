import math

# 将值限制在一个范围内
def clamp(value, min, max):
    if value < min: return min
    if value > max: return max
    return value

# 计算两点之间的距离
def distance(x, y, Px, Py):
    return math.sqrt(math.pow(x - Px, 2) + math.pow(y - Py, 2))
    