def resistor_label(colors):
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
    dict_of_tolerance = {
        "grey": "0.05%",
        "violet":"0.1%",
        "blue": "0.25%",
        "green": "0.5%",
        "brown": "1%",
        "red": "2%",
        "gold": "5%",
        "silver":"10%"
    }
    metric_prefix = {
    "giga": 1000000000,
    "mega": 1000000,
    "kilo": 1000
    }
    prefix = " ohms"
    if len(colors) == 1:
        main_value = int(str(dict_of_colors[colors[0]]))
        return(str(int(main_value)) + prefix)
    elif len(colors) == 4: 
        main_value = int(str(dict_of_colors[colors[0]]) + str(dict_of_colors[colors[1]]) + str(dict_of_colors[colors[2]]*"0"))
        tolerance = " ±" + dict_of_tolerance[colors[3]]
    else:
        main_value = int(str(dict_of_colors[colors[0]]) + str(dict_of_colors[colors[1]]) + str(dict_of_colors[colors[2]]) + str(dict_of_colors[colors[3]]*"0"))
        tolerance = " ±" + dict_of_tolerance[colors[4]]
    for k,v in metric_prefix.items():
        if main_value >= v:
            main_value /=v
            prefix = " " + k + "ohms"
            break
    
    
    if main_value % 1 == 0:
        main_value = int(main_value)
    return(str(main_value) + prefix + tolerance)
