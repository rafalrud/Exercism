import math

def score(x, y):
    points = 0
    cords = math.hypot(x, y)
    if cords <= 1:
        points = 10
    elif cords <= 5:
        points = 5
    elif cords <= 10:
        points = 1
    
    return points
