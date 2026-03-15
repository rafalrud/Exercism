def is_valid(isbn):
    clean = isbn.replace(" ", "").replace("-", "") 
    if len(clean) != 10:
        return False
    if not clean[-1].isdigit() and not clean[-1].lower() == "x":
        return False
    numbers = [ number for number in clean if number.isdigit() or number.lower() == "x" ]
    total = 0
    for counter, value in enumerate(numbers):
        if value.lower() == "x":
            if counter != 9:
                return False
            else:
                value = 10
        else:
            value = int(value)
        total += (counter+1) * value
    return bool(total % 11 == 0)
        
    
