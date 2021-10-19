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
