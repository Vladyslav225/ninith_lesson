# def line(_str, size):
#      a = _str * size
#      return a

# def line_sharp( _str, size, isspace=False):
#      a = ''

#      for _ in range(size):
#           if not isspace:
#                a += '*\n'

#           elif isspace:
#                aa = '**'
#                for i in range(17):
#                     aa += '#'
               
#                a = aa + '**\n'

# #           elif isspace:
# #                aa = '##**'
# #                for i in range(13):
# #                     aa += '%'
               
# #                a = aa + '**##\n'

# #           elif isspace:
# #                aa = '%%##**'
# #                for i in range(9):
# #                     aa += '^'
               
# #                a = aa + '**##%%\n'

#      return a

# a = line('*', 21)
# ab = line_sharp('a', 1, isspace=True)
# print(a)
# print(ab.rstrip())
# print(a)





# Converter
list_line = []

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

     print()
     line = second_line()
     print(line)
     line = second_line()
     print(line)
     line = second_line()
     print(line)
     line = second_line()
     print(line)
     line = second_line()
     print(line)
     line = second_line()
     print(line)
     line = first_line()
     print(line)
     print()



def func_l():

     line = third_line()
     print(line)
     line = third_line()
     print(line)
     line = third_line()
     print(line)
     line = third_line()
     print(line)
     line = third_line()
     print(line)
     line = third_line()
     print(line)
     line = first_line()
     print(line)

     return line

# print(func_l())

def func_a():

     print()
     line = first_line()
     print(line)
     line = second_line()
     print(line)
     line = second_line()
     print(line)
     line = first_line()
     print(line)
     line = second_line()
     print(line)
     line = second_line()
     print(line)
     line = second_line()
     print(line)
     print()


     # return 'a'

# print(func_a())

def func_d():

     print()
     line = first_line()
     print(line)
     line = second_line()
     print(line)
     line = second_line()
     print(line)
     line = second_line()
     print(line)
     line = second_line()
     print(line)
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