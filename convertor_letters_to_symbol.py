# Converter


list_letters = []

word_list = 'vlad'

width_line = 10


def first_line():

     line_0 = '#' * width_line

     return line_0

def second_line():

     line_1 = '##'

     for _ in range(6):
          line_1 += '.'
     
     line_1 += '##'

     return line_1

def third_line():

     line_2 = '##'

     for _ in range(8):
          line_2 += '.'

     return line_2   

def func_v():

     for _ in range(6):
          line = second_line()
          print(line)

     line = first_line()
     print(line)
     print()



def func_l():

     for _ in range(6):
          line = third_line()
          print(line)

     line = first_line()
     print(line)
     print()

def func_a():

     line = first_line()
     print(line)

     for _ in range(2):
          line = second_line()
          print(line)
     
     line = first_line()
     print(line)

     for _ in range(3):
          line = second_line()
          print(line)
     print()

def func_d():

     print()
     line = first_line()
     print(line)

     for _ in range(5):
          line = second_line()
          print(line)
     
     line = first_line()
     print(line)

line_dict = {
     'v': func_v(),
     'l': func_l(),
     'a': func_a(),
     'd': func_d()
     }