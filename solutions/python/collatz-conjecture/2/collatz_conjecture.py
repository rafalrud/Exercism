def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    steps_counted = 0
    while number != 1:          
        steps_counted += 1
        number = number / 2 if number % 2 == 0 else number * 3 +1  
    return steps_counted