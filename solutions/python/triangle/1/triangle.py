def equilateral(sides):
    if sum(sides) > 0:
        a,b,c = sides
        return a == b == c
    return False

def isosceles(sides):
    if sum(sides) > 0:
        a,b,c = sides
        if (a + b > c) and (a + c > b) and (b + c > a):
            return a == b or b == c or a ==c 
    return False


def scalene(sides):
    a,b,c = sides
    if (a + b > c) and (a + c > b) and (b + c > a):
        return a != b != c != a
    return False
