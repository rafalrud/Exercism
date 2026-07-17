def label(colors):
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
                    "white": 9}
    metric_prefix = {
    "giga": 1000000000,
    "mega": 1000000,
    "kilo": 1000
    }
    prefix = ""
    main_value = int(str(dict_of_colors[colors[0]]) + str(dict_of_colors[colors[1]]) + str(dict_of_colors[colors[2]]*"0"))
    print(main_value)
    for k,v in metric_prefix.items():
        if main_value > v:
            main_value /=v
            prefix = k
            break
    
    return str(int(main_value)) + " " + prefix + "ohms"