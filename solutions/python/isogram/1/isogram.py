def is_isogram(string):
    seen = []
    for char in string.lower().strip():
        if not char.isalpha():
            continue
        elif char in seen:
            return False
        else:
            seen.append(char)
    return True
