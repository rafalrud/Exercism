def is_pangram(sentence):
    if len(sentence.strip()) < 26:
        return False
    seen = [False] * 26
    for char in sentence:
        if "a" <= char.lower() <= "z":
            seen[ord(char.lower()) - ord("a")] = True
    return all(seen)
