def value(colors):
    dict_of_colors = {
                    "black": 0,
                    "brown": 1,
                    "red": 2,
                    "orange": 3,
                    "yellow": 4,
                    "green": 5,
                    "blue": 6,
                    "violet": 7,
                    "grey": 8,
                    "white": 9,
    }
    return int(str(dict_of_colors[colors[0]]) + str(dict_of_colors[colors[1]])) 