# FOR LOOPS:
# for item in 'Python':
#     print(item)

# for item in ['Jimmy', 'Mandy', 'Sock']:
#     print(item)

# for item in [1, 2, 3, 4]:
#     print(item)

# Below: Iterate over a large list of numbers:
# for item in range(40):
#     print(item)

# Below: Will show numbers between 3 and 10. Includes 3 but EXCLUDES 10
# for item in range(3, 10):
#     print(item)

# Below: The last number will be implemented as step. Meaning numbers will print adding 2. (3, 5, 7 ect. )  
# for item in range(3, 10, 2):
#     print(item)

# EXERCISE:
# SHOPPING CART TOTAL CALCULATION:
# prices = [10, 20, 30]
# total = 0

# for cost in prices:
#     total += cost

# print(f"Total: {total}")

# NESTED LOOPS: To generate coordinates.
# for x in range(4):
#     for y in range(3):
#         print(f"({x},{y})")

# CHALLENGE: MAKE AN 'F' WITH X'S. Don't forget--- Indents will change how the code is executed.
# numbers = [5, 2, 5, 2, 2]

# for x_count in numbers:
#     output = ''
#     for count in range(x_count):
#         output += 'x'
#     print(output)