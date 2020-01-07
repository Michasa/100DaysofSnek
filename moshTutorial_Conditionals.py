import math
is_hot = False
is_cold = True

# don't forget the colons when starting blocks
# else if in Python is elif, wtf...

if is_hot:
    print('its hot baby')
elif is_cold:
    print('naw its cold ')
else:
    print('nah its all goood')
print('end')


# Exercise 1
house_price = 10**6
is_buyer_credit_good = False
good_credit_percentage = 0.1
bad_credit_percentage = 0.2
has_high_income = True

if is_buyer_credit_good:
    down_payment = round(house_price * good_credit_percentage)
if not is_buyer_credit_good:
    down_payment = round(house_price * bad_credit_percentage)
print(f'Please pay ${down_payment}')

# and, or, not are python equivalents to javascript &&, || and !!

temperature = 50

if temperature > 30:
    print('its a very hot day')
else:
    print('its cooler')

# Exercise 2
name = input('what is your name?')
name_length = len(name)
if name_length < 3:
    message = 'please choose more than 3 characters'
elif name_length > 10:
    message = 'please choose something less than 50 characters'
else:
    message = f'fabulous name, {name}'
print(message)

# Exercise 3
weight = input('Weight: ')
unit = input('Is that (l)bs or (k)gs?: ')
conversion_rate = 2.205

if unit.upper() == 'L':
    conversion = math.ceil(int(weight) / conversion_rate)
    print(f'you are {conversion}kgs')
elif unit.upper() == 'K':
    conversion = math.ceil(int(weight) * conversion_rate)
    print(f'you are {conversion}lbs')
else:
    print('error, unit not recognised')
