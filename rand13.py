import random

# We assume rand11() is a blackbox
def rand11():
    num = random.randint(1,11)
    return num

def rand13():

    # Create a 11x11 matrix and initialize all elements to zero
    Matrix = [[0 for x in range(11)] for i in range(11)]

    # The last index that we can modify
    maxIndex = 13*(121//13)

    # Set values in array from 1-> 13 consecutively
    for i in range(11):
        for j in range(11):
            currentIndex = 11 * i + j
            if (currentIndex < maxIndex):
                Matrix[i][j] = (11 * i + j) % 13 + 1

    # The matrix that we will use to find a random element from 1-13
    # printMatrix(Matrix)

    # We found the result of rand13() when result != 0
    # then, result would be an int from 1-13
    result = 0
    while (result == 0):
        # randomize the index of row and column of matrix
        row = rand11() - 1
        col = rand11() - 1
        result = Matrix[row][col]

    return result
        

def printMatrix(matrix):
    print(matrix)
    for i in range(len(matrix)):
        print(matrix[i])

print(rand13())