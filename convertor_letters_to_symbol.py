# Converter


# list_letters = []

# width_line = 10


# def first_line():

#      line_0 = '#' * width_line

#      return line_0

# def second_line():

#      line_1 = '##'

#      for _ in range(6):
#           line_1 += '.'
     
#      line_1 += '##'

#      return line_1

# def third_line():

#      line_2 = '##'

#      for _ in range(8):
#           line_2 += '.'

#      return line_2



# def func_v():

#      for _ in range(6):
#           line = second_line()
#           print(line)

#      line = first_line()
#      print(line, '\n')


# def func_l():

#      for _ in range(6):
#           line = third_line()
#           print(line)

#      line = first_line()
#      print(line, '\n')

# def func_a():

#      line = first_line()
#      print(line)

#      for _ in range(2):
#           line = second_line()
#           print(line)
     
#      line = first_line()
#      print(line)

#      for _ in range(3):
#           line = second_line()
#           print(line)
#      print()

# def func_d():

#      line = first_line()
#      print(line)

#      for _ in range(5):
#           line = second_line()
#           print(line)
     
#      line = first_line()
#      print(line)

# line_dict = {
#      'v': func_v(),
#      'l': func_l(),
#      'a': func_a(),
#      'd': func_d()
#      }






width_line = 10


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

     line_v_0 = second_type_line()
     line_v_1 = second_type_line()
     line_v_2 = second_type_line()
     line_v_3 = second_type_line()
     line_v_4 = second_type_line()
     line_v_5 = second_type_line()
     line_v_6 = first_type_line()

     res = line_v_0 + '\n' + line_v_1 + '\n' + line_v_2 + '\n' + line_v_3 + '\n' + line_v_4 + '\n' + line_v_5 + '\n' + line_v_6

     return res

def func_l():

     line_v_0 = third_type_line()
     line_v_1 = third_type_line()
     line_v_2 = third_type_line()
     line_v_3 = third_type_line()
     line_v_4 = third_type_line()
     line_v_5 = third_type_line()
     line_v_6 = first_type_line()

     res = line_v_0 + '\n' + line_v_1 + '\n' + line_v_2 + '\n' + line_v_3 + '\n' + line_v_4 + '\n' + line_v_5 + '\n' + line_v_6

     return res

def func_a():

     line_v_0 = first_type_line()
     line_v_1 = second_type_line()
     line_v_2 = second_type_line()
     line_v_3 = first_type_line()
     line_v_4 = second_type_line()
     line_v_5 = second_type_line()
     line_v_6 = second_type_line()

     res = line_v_0 + '\n' + line_v_1 + '\n' + line_v_2 + '\n' + line_v_3 + '\n' + line_v_4 + '\n' + line_v_5 + '\n' + line_v_6

     return res

def func_d():

     line_v_0 = first_type_line()
     line_v_1 = second_type_line()
     line_v_2 = second_type_line()
     line_v_3 = second_type_line()
     line_v_4 = second_type_line()
     line_v_5 = second_type_line()
     line_v_6 = first_type_line()

     res = line_v_0 + '\n' + line_v_1 + '\n' + line_v_2 + '\n' + line_v_3 + '\n' + line_v_4 + '\n' + line_v_5 + '\n' + line_v_6

     return res

dict_letters = {
     'v': func_v(),
     'l': func_l(),
     'a': func_a(),
     'd': func_d()
     }

for key in dict_letters:
     print(dict_letters[key] + '\n')

with open('convert.txt', 'w') as convert:
     for key in dict_letters:
          convert.write(dict_letters[key] + '\n')
          convert.close
