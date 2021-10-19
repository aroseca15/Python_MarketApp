# 2D LISTS: used for data that are and have to be stored in rectangular data table. 2D arrays are known as matrices which we will use.

# [
#     1 2 3
#     4 5 6
#     7 8 9
# ]
# In math this is a 3x3 matrix. This can be modeled using 2D lists. Basically, the computer will understand that each item of the top list will have their own lists.

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# Below: The number in the first brackets indicates the selected index for the first list (horizontally). The number in the second brackets indicate the selected index place inside the first bracket list. Here 2 would be printed since it's the first list [0] second item [1].

# print(matrix[0] [1])


# If we needed to modify an item in the matrix this is how:
# matrix[0] [1] = 20
# print(matrix[0] [1])

# We can also use nested for loops to iterate over all the items in the matrix. in each row will contain one list, one item.
# for row in matrix:
#     for item in row:
#         print(item)
