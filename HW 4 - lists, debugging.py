#2 Practicing Sliding & Striding

#2.1: Making a List Variable

number_of_lipglosses = list(range(21))
print(number_of_lipglosses)


#2.2: Working with List Elements

def squared_List(lst):
    return [x**2 for x in lst]

squared_list = squared_List(number_of_lipglosses)
print(squared_list)

#2.3: Slicing

def get_first_fifthteen(lst):
    return lst[0:16]
first_fifthteen_elements = get_first_fifthteen(squared_list)
print(first_fifthteen_elements)

#2.4: Striding

def striding_list(lst):
    return lst[4:21:5]
every_fifth_element= striding_list(squared_list)
print(every_fifth_element)

#2.5: Slicing & Striding
def slicing_and_striding(lst):
    return lst[-1::-3]
slicing_and_striding_result = slicing_and_striding(squared_list)
print(slicing_and_striding_result)

# 3:2D Lists
# 3.1: Creating a 5x5 2D List

def create_2d_list():
    return [[col + row * 5 + 1 for col in range(5)] for row in range(5)]

matrix = create_2d_list()

for row in matrix:
    print(row)

def create_2d_list():
    return [[col + row * 5 + 1 for col in range(5)] for row in range(5)]

def modified_2d_list(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] % 3 == 0:
                matrix[row][col] = "?"
    return matrix

def sum_non_question_elements(matrix):
    total = 0
    for row in matrix:
        for item in row:
            if item != "?":
                total += item
    return total

matrix = create_2d_list()
new_matrix = modified_2d_list(matrix)
result = sum_non_question_elements(new_matrix)

for row in new_matrix:
    print(row)

print("Sum of non-'?' elements:", result)

