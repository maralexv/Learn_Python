import random

# Global list of possible values in the matrix
options = [0,1,2,3]

def initialise_matrix():
    # Initialise the matrix
    return [[0,0,0,0,0,0],[0,8,1,8,8,0],[0,2,3,8,8,0],[0,8,8,8,0,0],[0,8,8,8,8,0],[0,0,0,0,0,0]]

# m = initialise_matrix()
# print (m)

def check_if_field_empty(matrix,y,x):
    # Check if a given field in the matrix is empty
    if matrix[y][x] == 8:
        return True
    else:
        return False

# print (check_if_field_empty(m, 1, 2))

def check_if_around_empty(matrix,y,x):
    # Check if any of the fields surraunding the given field are empty
    if matrix[y-1][x-1] == 8 or matrix[y-1][x] == 8 or matrix[y-1][x+1] == 8 or matrix[y][x-1] == 8 or matrix[y][x+1] == 8 or matrix[y+1][x-1] == 8 or matrix[y+1][x] == 8 or matrix[y+1][x+1] == 8:
        return True
    else:
        return False

# m = initialise_matrix()
# print (check_if_around_empty(m,1,1))
# print(check_if_around_empty(m,1,3))

def check_if_matrix_incomplete(matrix):
    check_var = True
    # Check if there are any empty fields (8) left in the matrix
    for y in range(1,5):
        for x in range(1,5):
            if matrix[y][x] == 8:
                check_var = True
            else:
                check_var = False
    return check_var


# m = initialise_matrix()
# print(m)
# print(check_if_matrix_incomplete(m))
#
# newm = [[1,2,3,4,5,6,7],[5,1,0,9,10],[2,5,6,9,4],[1,0,0,0,7]]
# print(newm)
# print(check_if_matrix_incomplete(newm))


def check_if_matrix_correct(matrix):
    check_var = []
    # Check if every field in the matrix satisfies defined conditons
    for y in range(1,5):
        for x in range(1,5):
            sur_fields_sum = matrix[y-1][x-1] + matrix[y-1][x] + matrix[y-1][x+1] + matrix[y][x-1] + matrix[y][x+1] + matrix[y+1][x-1] + matrix[y+1][x] + matrix[y+1][x+1]
            if matrix[y][x] == (sur_fields_sum % 4):
                None
            else:
                check_var.append(1)
    if 1 in check_var:
        return False
    else:
        return True


def solve_matrix():
    # Initialise matrix
    matrix = initialise_matrix()
    # Start algorithm
    while check_if_matrix_incomplete(matrix):
        for y in range(1,5):
            for x in range(1, 5):
                if check_if_field_empty(matrix, y, x):
                    if check_if_around_empty(matrix, y, x):
                        matrix[y][x] = random.choice(options)
                    else:
                        sur_fields_sum = matrix[y-1][x-1] + matrix[y-1][x] + matrix[y-1][x+1] + matrix[y][x-1] + matrix[y][x+1] + matrix[y+1][x-1] + matrix[y+1][x] + matrix[y+1][x+1]
                        matrix[y][x] = sur_fields_sum % 4

    if check_if_matrix_correct(matrix):
        print(matrix)
        print("CORRECT!")
    else:
        print(matrix)
        print("INCORRECT!!!")
        solve_matrix()


solve_matrix()
