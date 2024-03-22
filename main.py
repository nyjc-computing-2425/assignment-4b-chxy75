stdform = input('Enter a number in scientific notation: ')
stdform = stdform.strip()
symbols = ['.', 'x', '^']
chars = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', 'x', '^', '-', 'E'
]
char_valid = True
count_valid = True
int_valid = True
man_valid = True

# Type your code below
for char in stdform:
  if char in chars:
    char_valid = True
    #print("a")
  else:
    char_valid = False
    #print('b')

for symbol in symbols:
  if stdform.count(symbol) <= 1:
    count_valid = True
   # print("c")
  else:
    count_valid = False
    #print('d')

stdform = ''.join(stdform)

if stdform[0] == '-':
  ex = float(stdform[stdform.find('^') + 1:].strip(' ').strip('-'))
else:
  ex = float(stdform[stdform.find('^') + 1:].strip(' '))

if ex.is_integer():
  int_valid = True
  #print("e")
else:
  int_valid = False
  #print('f')

man = stdform[:stdform.find('x')].strip(' ').strip('-').replace('.','')
#print(man)
if man.isdigit():
  man_valid = True
  #print('g')
else:
  man_valid = False
  #print('h')

if (char_valid is True) and (count_valid is True) and (int_valid is True) and (man_valid is True):
  exponent = stdform[stdform.find('^') + 1:].strip(' ')
  mantissa = stdform[:stdform.find('x')].strip(' ')
  E = mantissa + 'E' + exponent + "."
  print('This number in E notation is', E)

else:
  print('Error converting to scientific E notation.')
