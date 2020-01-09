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
# Car
car_started = False
# Strings
car_start_string = 'Car started...Ready to go! 🚗'
car_stopping_string = 'Car stopped! 🛑'
quit_string = 'Goodbye 👋'
command_not_found_string = 'Sorry I do not understand 🤷‍♀'
already_started = 'car already started!'
already_stopped = 'call already stopped'
help_string = '''
== possible commands ==
start - start your engines gentlemen!
stop - stop your car hunny
quit - to exit and shantaya away
status - is the car running or nah?
'''

while True:
    user_input = (input('> ')).upper()
    if user_input == 'START':
        if not car_started:
            car_started = True
            print(car_start_string)
        else:
            print(already_started)
    elif user_input == 'STOP':
        if car_started:
            car_started = False
            print(car_stopping_string)
        else:
            print(already_stopped)
    elif user_input == 'HELP':
        print(help_string)
    elif user_input == 'QUIT':
        car_started = False
        print(quit_string)
        break
    else:
        print(
            "sorry,I don't recognise that command. Enter `help` to show possible commands")
