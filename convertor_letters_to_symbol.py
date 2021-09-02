width_line = 10

list_letters = 'vlad'

def first_type_line():

     line_0 = '#' * width_line

     return line_0

def second_type_line():

     line_1 = '##'

     for _ in range(6):
          line_1 += '.'
     
     line_1 += '##'

     return line_1

def third_type_line():

     line_2 = '##'

     for _ in range(8):
          line_2 += '.'

     return line_2

def func_v():

     res = ''

     for _ in range(6):
          res += second_type_line() + '\n'

     res += first_type_line()
     return res

def func_l():

     res = ''

     for _ in range(6):
          res += third_type_line() + '\n'

     res += first_type_line()

     return res

def func_a():

     res = first_type_line() + '\n'

     for _ in range(2):
          res += second_type_line() + '\n'

     res += first_type_line() + '\n'

     for _ in range(3):
          res += second_type_line() + '\n'

     return res

def func_d():

     res = first_type_line() + '\n'

     for _ in range(6):
          res += second_type_line() + '\n'

     res += first_type_line()

     return res

dict_letters = {
     'v': func_v(),
     'l': func_l(),
     'a': func_a(),
     'd': func_d()
     }

for letter in list_letters:
     dict_letters[letter]

for key in dict_letters:
     print(dict_letters[key], '\n')

with open('convert.txt', 'w') as convert:
     for key in dict_letters:
          convert.write(dict_letters[key] + ('\n'))
          convert.close
