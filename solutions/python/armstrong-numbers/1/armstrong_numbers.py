def is_armstrong_number(number):
    if not number == 0:
        digits = str(number)
        power = len(digits)
        return number == sum( int(x) ** power for x in digits)
    return True