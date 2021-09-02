def star_converter(_str, size):

     res = _str * size
     return res



def sharpe_converter():
     pass

def procent_converter():
     pass

def stepper_converter():
     pass

def at_converter():
     pass

dict_converters = {
     'a': star_converter,     # '*'
     'b': sharpe_converter,   # '#'
     'c': procent_converter,  # '%'
     'd': stepper_converter,  # '^'
     'e': at_converter        # '@'
}

line_1 = star_converter('*', 21)
line_2 = star_converter('#', 21)
line_3 = star_converter('%', 21)
line_4 = star_converter('', 21)
line_5 = star_converter('*', 21)
line_6 = star_converter('*', 21)
line_7 = star_converter('*', 21)
line_8 = star_converter('*', 21)
line_9 = star_converter('*', 21)
print(line_1)
