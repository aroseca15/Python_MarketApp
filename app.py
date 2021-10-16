# price = 10
# rating = 4.9
# first_name = 'John'
# last_name = 'Smith'
# age = 20
# is_newPatient = True
# print(first_name, last_name, age, is_newPatient)

# name = input('What is your name? ')
# print('Hi ' + name)

# fav_color = input('Nice to meet you. What is your favorite color? ')
# print('Wow, I love ' + fav_color)
# print(name + ' loves ' + fav_color)

# birth_year = input('Birth year: ')
# print(type(birth_year))
# age = 2021 - int(birth_year)
# print(type(age))
# print(age)

# weight = input('Please, enter your weight in lbs: ')

# convert_weight = int(weight) * 0.45

# print(convert_weight)

# STRINGS:
# course = '''     
# Hi Family,
# I want you to know that I Love You so much! 
# Love You,
# Mandy
# '''
# print(course)

# course2 = 'Python for Beginners'

# print(course2[0:3])

# FORMATTED STRINGS:
# first_name = 'John'
# last_name = 'Smith'

# Below not the best:
# message = first_name + ' [' + last_name + '] is a coder.'
# print(message)

# Formatted string below is more ideal:
# msg = f'{first_name} [{last_name}] is a coder'
# print(msg)

# STRING METHODS:    ALL methods are case sensitive.
# course = 'Python For Beginners'
# len() calculates # of characters in the string. (Helpful for inforcing a character limit in a user input field. Is a general function that can also be used for a list.)
# print(len(course))

# print(course.upper())
# print(course.lower())
# print(course.find('Beginners'))
# print(course.replace('Beginners', 'Masters'))

# Below is the [ in ] opporator, this will return a boolean value if what is specified is True or False.
# print('Python' in course)
# course.title() = The title method will turn every first letter as an uppercase. Example: (hello world!) will return (Hello World!) OR if there is a letter that follows a non alphabetical character then that is following letter is uppercase. Example: (he11o w0r1d) returns as (He11O W0R1D).

# ARITHMETIC OPERATIONS:
# print(10 + 3)
# print(10 - 3)
# print(10 / 3)
# Below is a division that will only return the int value, not the float.
# print(10 // 3)
# Below is the operator modulis and it will return the remainder of the division as an int.
# print(10 % 3)
# Below is the operator power or exponent and it will return 10 to the power of 3 .
# print(10 ** 3)
# Below is the augmented assignment operator. This is useful for
# x = 10
# adds 3
# x+=3

# subtracts 3
# x-=3


# same as below
# x = 10
# x = x + 3

# print(x)

# OPERATOR PRECEDENCE: Basically, order of operations.
# x = (2 + 3) * 10 - 3
# print(x)

# MATH FUNCTIONS: round(), abs() absolute, Math Calculation Modules,
# import math

# print(math.ceil(2.9))
# print(math.floor(2.9))

# x = 2.9

# print(round(x))
# print(abs(-2.9))

# IF STATEMENTS:
# is_hot = False
# is_cold = False

# if is_hot: 
#     print("It's a hot day")
#     print("Drink plenty of water.")
# elif is_cold:
#     print("It's a cold day.")
#     print("Drink lots of water and wear warm clothes.")
# else:
#     print("Enjoy your day. Because the weather is perfect!")
# print(

# MY SOLUTION:
# has_good_credit = True
# price_of_house = 1000000

# if has_good_credit:
#     down_payment = price_of_house * .1
#     print(round(down_payment))
# else:
#     down_payment = price_of_house * .2
#     print(round(down_payment))

# MOSH'S SOLUTION:
# has_good_credit = True
# price = 1000000

# if has_good_credit:
#     down_payment = price * .1
# else:
#     down_payment = price * .2

# print(f"Down Payment: ${down_payment}")

# LOGICAL OPERATIONS: AND => combines two conditions that both need to be met for and outcome. OR => will do what is expected is at least one condition is true. NOT => indicates what conditions need to be False in order to respond.
# has_high_income = True
# has_good_credit = False
# has_criminal_record = True

# if has_good_credit and has_high_income:
#     print("Eligible for loan.")

# if has_good_credit or has_high_income:
#     print("Eligible for loan with conditions.")

# if has_good_credit or has_high_income and not has_criminal_record:
#     print("Eligible for loan with conditions.")


# COMPARISION OPERATIONS:
# temperature = 3

# if temperature >= 30:
#     print("Man, it's too hot today!")
# elif temperature < 4:
#     print("Woooo! It's cold!! Too Cold! I need Jimmy to cuddle with me!")
# else:
#      print("It's not too bad today. Actually nice!")


# Enforcing a Character Limit: MY SOLUTION:
# name_characters = 30

# if name_characters < 3:
#     print("Your name is too short.")
# elif name_characters > 50:
#     print("Your name exceeds the character limit.")
# else:
#     print("Looks good! Thank you.")

# Enforcing a Character Limit: MOSH'S SOLUTION:
# name = "Jimmy"
# print(len(name))
# if len(name) < 3:
#     print("Your name is too short.")
# elif len(name) > 50:
#     print("Your name exceeds the character limit.")
# else:
#     print("Looks good! Thank you.")

# FIRST PROJECT: WEIGHT CONVERTER:
# weight = input("Weight: ")

# unit = input("(L)lbs or (K)g: ")

# if unit == "l":
#     convert_weight = int(weight) * 0.45
#     print(f"You are {convert_weight} kilograms")
# elif unit == "k":
#     convert_weight = int(weight) * 2.2
#     print(f"You are {convert_weight} pounds")
# else:
#     print("I can only covert between lbs and kilograms for now. Try Again.")

# For some reason the calculations for the convert_weight are not working correctly. UPDATE: I forgot to format the string with f.

# MOSH'S SOLUTION:
# weight = int(input("Weight: "))
# unit = input("(L)lbs or (K)g: ")

# if unit.upper() == "L":
#     converted = weight * 0.45
#     print(f"You are {converted} kilos")
# else:
#     converted = weight / 0.45
#     print(f"You are {converted} pounds")


# WHILE LOOPS: As long as the condition is True it continues to repeat operate. But terminates when False.
# i = 1

# while i <= 5:
    # print(i)

    # This can work with symbols as well:
#     print('*' * i)

#     i = i + 1
# print("Done")

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
command = ""
started = False
# stopped = True

while True:
    command = input(">").lower()
    if command == "start":
        if started == True:
            print("Car is running")
        else:
            started = True
            print("Vroom! Vroom!")
    elif command == "stop":
        if started == False:
            print("Car is at a complete stop already.")
        else:
            started = False
            print("Sqeeeek, stopped.")
    elif command == "help":
        print(''' 
start - to start the car
stop - to stop the car
quit - to quit
            ''')
    elif command == "quit":
        break
    else:
        print("Sorry, I do not understand that command.")
