def response(hey_bob):
    hey_bob = hey_bob.strip()
    if hey_bob == "":
        return "Fine. Be that way!"
    if hey_bob.endswith("?") and hey_bob.upper() == hey_bob and any(c.isalpha() for c in hey_bob):
        return "Calm down, I know what I'm doing!"
    if hey_bob.upper() == hey_bob and any(c.isalpha() for c in hey_bob):
        return "Whoa, chill out!"
    if hey_bob.endswith("?"):
        return "Sure."
    return "Whatever." 
