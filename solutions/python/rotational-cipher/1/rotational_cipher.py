def rotate(text, key):
    alphabet ="abcdefghijklmnopqrstuvwxyz"
    new_text = ""
    key = key % 26
    for letter in text:
        id = alphabet.find(letter.lower())

        if id == -1:
            new_text += letter
        else:
            rotated_id = (id + key) % 26
            new_letter = alphabet[rotated_id]
            if letter.isupper():
                new_letter = new_letter.upper()
            new_text += new_letter

    return new_text