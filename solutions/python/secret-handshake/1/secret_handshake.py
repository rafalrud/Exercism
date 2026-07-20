def commands(binary_str):

    secret_handshake = []
    actions = {
        1 : "wink",
        2 : "double blink",
        4 : "close your eyes",
        8 : "jump",
        16 : "reverse"
    }
     
    while binary_str != "":
        power = pow(2,len(binary_str)-1)
        print(power)
        if int(binary_str,2) >= power:
            secret_handshake.append(actions[power])
        binary_str = binary_str[1:]
    secret_handshake.reverse()
    if "reverse" in secret_handshake:
        secret_handshake.remove("reverse")
        secret_handshake.reverse()

    return secret_handshake