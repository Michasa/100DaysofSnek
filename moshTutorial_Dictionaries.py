# This is basically Python version of objects
customer = {
    "name": "Olivia",
    "age": 30,
    "knows_python": True
}

# It is immutable
customer["age"] = 31
customer["profession"] = "coder"
print(customer)


# the methog .get() is a kinder way to check for the existance of properties rather than through indexing. It returns 'None'
print(customer.get('purchase'))

# Exercise
numerals = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: "six",
    7: "seven",
    8: "eight",
    9: 'nine'
}

given_number = input('Phone (Intergers_Only)☎️: ')

numeral_string = ''

for digit in given_number:
    if numerals.get(digit):
        numeral_string += f'{numerals.get(digit,"*")} '
    else:
        print("*")
print(numeral_string)

# Exercise
message = input("> ")
message = message.split(' ')

emojis = {
    ":)": "😄",
    ":'(":  "😢",
    ":/": "😕"
}
output = ''
for word in message:
    output += emojis.get(word, word) + " "
print(output)
