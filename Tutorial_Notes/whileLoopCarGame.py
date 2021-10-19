# BUILDING A GUESSING GAME QUICK PROJECT:
# secret_number = 7
# i = 0     I renamed the i as guess_count
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input('Guess the number I am thinking: '))
#     guess_count += 1
#     if guess == secret_number:
#         print('You Won!')
#         break
# else:
#     print('Sorry, you are out of guesses.')


# CAR GAME QUICK PROJECT: Started with project today. Still working on applying what is learned.
# Mosh's Solution: Best to attach methods right at input, if using triple quotes remember not to have un-needed indents. Otherwise the indents will show on the terminal. Some of Mosh's solution was not producing the needed results for car already running or stopped. So I made minor adjustments.
# command = ""
# started = False
# stopped = True

# while True:
#     command = input(">").lower()
#     if command == "start":
#         if started == True:
#             print("Car is running")
#         else:
#             started = True
#             print("Vroom! Vroom!")
#     elif command == "stop":
#         if started == False:
#             print("Car is at a complete stop already.")
#         else:
#             started = False
#             print("Sqeeeek, stopped.")
#     elif command == "help":
#         print(''' 
# start - to start the car
# stop - to stop the car
# quit - to quit
#             ''')
#     elif command == "quit":
#         break
#     else:
#         print("Sorry, I do not understand that command.")
