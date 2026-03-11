def square(number):
    if not 1 <= number < 65:
        raise ValueError("square must be between 1 and 64")
    counter = 1
    for _ in range (1, number):
        counter *= 2
    return counter


def total():
    return sum(square(i) for i in range(1,65))
