import math
is_hot = False
is_cold = True

# don't forget the colons when starting blocks
# else if in Python is elif, wtf...

if is_hot:
    print('its hot baby')
elif is_cold:
    print('its cold naw')
else:
    print('nah its all goood')
print('end')


# Exercise 1
house_price = 10**6
is_buyer_credit_good = True
good_credit_percentage = 0.1
bad_credit_percentage = 0.2


if is_buyer_credit_good:
    down_payment = round(house_price * good_credit_percentage)
else:
    down_payment = round(house_price * bad_credit_percentage)
print(f'Please pay ${down_payment}')
