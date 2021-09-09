list_result_key = []

list_result_letters = []


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

     letter_v = ''

     for _ in range(6):
          letter_v += second_type_line() + '\n'

     letter_v += first_type_line()
     return letter_v

def func_l():

     letter_l = ''

     for _ in range(6):
          letter_l += third_type_line() + '\n'

     letter_l += first_type_line()

     return letter_l

def func_a():

     letter_a = first_type_line() + '\n'

     for _ in range(2):
          letter_a += second_type_line() + '\n'

     letter_a += first_type_line() + '\n'

     for _ in range(3):
          letter_a += second_type_line() + '\n'

     return letter_a

def func_d():

     letter_d = first_type_line() + '\n'

     for _ in range(5):
          letter_d += second_type_line() + '\n'

     letter_d += first_type_line()

     return letter_d

dict_letters = {'v': func_v(), 'l': func_l(), 'a': func_a(), 'd': func_d()}

for key in dict_letters:
     result_key = dict_letters[key]
     list_result_key.append(result_key)

get_index_v = list_result_key[0]
get_index_l = list_result_key[1]
get_index_a = list_result_key[2]
get_index_d = list_result_key[3]

split_letter_0 = get_index_v.split('\n')
split_letter_1 = get_index_l.split('\n')
split_letter_2 = get_index_a.split('\n')
split_letter_3 = get_index_d.split('\n')

for letter_0, letter_1, letter_2, letter_3 in zip(split_letter_0, split_letter_1, split_letter_2, split_letter_3):
     result_letters = letter_0 + '   ' + letter_1 + '   ' + letter_2 + '   ' + letter_3
     list_result_letters.append(result_letters)


for letters_in_one_line in list_result_letters:
     print(letters_in_one_line)

with open('Word_of_symbols.txt', 'w') as file:
     for letters_in_one_line in list_result_letters:
          file.write(letters_in_one_line + '\n')
          file.close