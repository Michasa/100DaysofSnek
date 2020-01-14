def weight_converter():
    print("Welcome to Weight Convertor 🏋️‍♀️")
    weight_lb = input('What is your weight in pounds? ')
    converstion_factor = 2.205
    result = int(weight_lb) / converstion_factor
    print('{} is your weight in kilograms'.format(round(result, 2)))


def emoji_convertor():
    print("Welcome to Emoji Convertor 👍 Write your sentence below")
    message = input("> ")
    emojis = {
        ":)": "😄",
        ":'(":  "😢",
        ":/": "😕"
    }

    message = message.split(' ')
    output = ""
    for word in message:
        output += emojis.get(word, word) + " "

    print(output)
