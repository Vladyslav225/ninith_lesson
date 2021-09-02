list_lines_symbol = []


def star_converter(_str, size):

     res = _str * size
     return res

def sharpe_converter(_str, size):
     
     symbol = '**'

     for _ in range(size):
          symbol += '#'

     symbol += '**'

     return symbol

def procent_converter(_str, size):

     symbol = '**##'

     for _ in range(size):
          symbol += '%'

     symbol += '##**'

     return symbol

def stepper_converter(_str, size):
     
     symbol = '**##%%'

     for _ in range(size):
          symbol += '^'

     symbol += '%%##**'

     return symbol

def at_converter(_str, size):
     symbol = '**##%%^^'

     for _ in range(size):
          symbol += '@'

     symbol += '^^%%##**'

     return symbol

def creating_picture():
     line_1 = star_converter('*', 20)
     line_2 = sharpe_converter('#', 16)
     line_3 = procent_converter('%', 12)
     line_4 = stepper_converter('^', 8)
     line_5 = at_converter('@', 4)
     line_6 = stepper_converter('^', 8)
     line_7 = procent_converter('%', 12)
     line_8 = sharpe_converter('#', 16)
     line_9 = star_converter('*', 20)
     
     res_picture = line_1 + '\n' + line_2 + '\n' + line_3 + '\n' + line_4 + '\n' + line_5 + '\n' + line_6 + '\n' + line_7 + '\n' + line_8 + '\n' + line_9

     return list_lines_symbol.append(res_picture)

creating_picture()

for line_symbol in list_lines_symbol:
     print(line_symbol, '\n')

with open('convert.txt', 'a') as convert:
     for line_symbol in list_lines_symbol:
          convert.write(line_symbol + ('\n'))
          convert.close