import random

def randLower(lower):
    num = random.randint(1, lower)
    return num

def randUpper(lower, upper):

    # Create a mxm matrix with m = lower
    # initialize all elements to zero
    Matrix = [[0 for x in range(lower)] for i in range(lower)]

    # The last index that we can modify
    maxIndex = upper * (lower ** 2 // upper)

    # Set values in array from 1-> 13 consecutively
    for i in range(lower):
        for j in range(lower):
            currentIndex = lower * i + j
            if (currentIndex < maxIndex):
                Matrix[i][j] = (lower * i + j) % upper + 1

    # The matrix that we will use to find a random element from 1-upper
    # printMatrix(Matrix)

    # We found the result of rand13() when result != 0
    # then, result would be an int from 1-upper
    result = 0
    attempts = 0
    while (result == 0):
        # randomize the index of row and column of matrix
        row = randLower(lower) - 1
        col = randLower(lower) - 1
        result = Matrix[row][col]
        attempts += 1

    return [result, attempts]

def printMatrix(matrix):
    print(matrix)
    for i in range(len(matrix)):
        print(matrix[i])

# Print multiple times to test the lowest, highest output,
# as well as attempts taken to find the result
for i in range(30):
    result = randUpper(5, 13)
    print("Output: {output}. Attempt(s): {attempts}".format(output=result[0], attempts=result[1]))