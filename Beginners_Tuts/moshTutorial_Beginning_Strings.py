### PRINTING ###
print('Hi World' * 8)
price = 10  # let price = 10
print(price)  # console.log(price * 10)

# name = 'john'
# age = '23'
# new_paitent = True
# print('my name is' + name + 'and I am' + age)

### INPUT ###
name = input('What is your name?😀 ')
color = input('What is your fav colour?🌈 ')
age = int(input('How old how are you?👶'))
new_age = age + 1
print('{0} likes {1}.{0} is {2} years old. Next year you will be {3} years old'.format(
    name, color, age, new_age))
print('Hi ', name)

weight_lb = input('What is your weight in pounds?')
converstion_factor = 2.205
result = int(weight_lb) / converstion_factor
print('{} is your weight in kilograms'.format(round(result, 2)))

name = input('enter a string ')
print('this was 2nd index of the string provided: {}'.format(name[2]))

### STRINGS ###
multi_line = '''
Dear Ellie,

Continue coding, it will serve you well.

From,
Future Elle
'''
print(multi_line)
print('That was {} characters long'.format(len(multi_line)))

start = multi_line[0:14].upper()

# Can replace matched strings with another
new = multi_line.replace('Ellie', 'Ellie Belly')

# Returns (start of) index of matched string
print(new.find('Ellie'))

# Return a boolean if string is contained in variable
print('Ellie' in new)
