list_rs =[]



width_line = 10

letters = 'vlad'

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

     letter = ''

     for _ in range(6):
          letter += second_type_line() + '\n'

     letter += first_type_line()
     return letter

def func_l():

     letter = ''

     for _ in range(6):
          letter += third_type_line() + '\n'

     letter += first_type_line()

     return letter

def func_a():

     letter = first_type_line() + '\n'

     for _ in range(2):
          letter += second_type_line() + '\n'

     letter += first_type_line() + '\n'

     for _ in range(3):
          letter += second_type_line() + '\n'

     return letter

def func_d():

     letter = first_type_line() + '\n'

     for _ in range(5):
          letter += second_type_line() + '\n'

     letter += first_type_line()

     return letter

dict_letters = {
     'v': func_v(),
     'l': func_l(),
     'a': func_a(),
     'd': func_d()
     }

for letter in letters:
     dict_letters[letter]

r1 = dict_letters['v']
r2 = dict_letters['l']
r3 = dict_letters['a']
r4 = dict_letters['d']

r_1 = r1.split('\n')
r_2 = r2.split('\n')
r_3 = r3.split('\n')
r_4 = r4.split('\n')

for rr_1, rr_2, rr_3, rr_4 in zip(r_1, r_2, r_3, r_4):
     rs = rr_1 + '   ' + rr_2 + '   ' + rr_3 + '   ' + rr_4
     list_rs.append(rs)

for r in list_rs:
     print(r)

with open('convert.txt', 'w') as convert:
     for r in list_rs:
          convert.write(r + '\n')
          convert.close
