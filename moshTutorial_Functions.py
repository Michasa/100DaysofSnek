def welcome_message(robot_name):
    print(f"hi there, I am {robot_name}")
    print("what is your name?")


# parameters = the placeholders in the function
# argument = the actual values given the function is called
welcome_message('Mr Robot!')


# you can set up key word argument, they explictly define which parameter that value is and so argument order doesn't matter. It can improve code readbility
def print_fullname(honorific, first_name, last_name):
    print(f"Hello {honorific}. {first_name} {last_name}")


#  However positional arguments come first and then key word argument
print_fullname('Mr', last_name='Bond', first_name='James')


# Functions that do not return anything will return None
def nothing():
    3+6


print(nothing())


# Exercise
def emoji_convertor(message, dictionary):
    message = message.split(' ')
    output = ""
    for word in message:
        output += dictionary.get(word, word) + " "

    return output


message = input("> ")
emojis = {
    ":)": "😄",
    ":'(":  "😢",
    ":/": "😕"
}

result = emoji_convertor(message, dictionary=emojis)

print(result)

# Exception Handling, allows defintion of better error messaging per error typ

try:
    age = int(input('Age >:'))
    result = 1000/age
    print(result)
except ZeroDivisionError:
    print('Please put in a number bigger than 0')
except ValueError:
    print('Invalid input. Numbers only please')
