def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    steps_counted = 0
    while True:
        if number == 1:
            return steps_counted        
        steps_counted += 1
        if number % 2 != 0:
            number = (number * 3) +1
        else:
            number = number // 2
