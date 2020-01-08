# # Example Guessing Game
# secret_number = 10
# guesses_left = 3


# while guesses_left > 0:
#     guess = int(input('Guess:'))

#     guesses_left = guesses_left-1
#     if(guess == secret_number):
#         print('congratz, you guessed the correct NUMBER')
#         break
# else:
#     print('no more chances 😞!')

# Car Game
car_start_string = 'Car started...Ready to go! 🚗'
car_stopping_string = 'Car stopped! 🛑'
quit_string = 'Goodbye 👋'
command_not_found = 'Sorry I do not understand 🤷‍♀'
help_string = '''
== possible commands ==
start - start your engines gentlemen!
stop - stop your car hunny
quit - to exit and shantaya away
'''

while True:
    user_input = (input('> ')).upper()
    if user_input == 'START':
        print(car_start_string)
    elif user_input == 'STOP':
        print(car_stopping_string)
    elif user_input == 'HELP':
        print(help_string)
    elif user_input == 'QUIT':
        print(quit_string)
        break
    else:
        print(
            "sorry,I don't recognise that command. Enter `help` to show possible commands")
