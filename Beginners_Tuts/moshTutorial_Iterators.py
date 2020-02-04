print('This shit is BANANAS,')
for item in 'Bananas':
    print(item.upper())
print('🍌\n')
harijuku_girls = ['Love 💗', 'Angel 👼', "Music 🎵", 'Baby 👶']

for member in harijuku_girls:
    print(member)

print('Hurry up and come and save me!\n')

# Range can be used to print out numbers between a certain range, the number specified is excluded so the numbers are from 0 to n-1.
# Can specifiy two other params: range(start_number, end_number(n-1), increment)
# so range(5,50,20) means start from 5 end at 49 and go up by 20 each time
for number in range(5):
    print(number)

# Exercise
prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(f'You total is: ${total}')

# Exercise 2
numbers = [5, 2, 5, 2, 2]
string = 'x'
for number in numbers:
    print(string*number)
