#naive algoithim:
#genereate all possible numbers for every square and generate evry possible combination of numbers for the square until the solution works, it works for every solution however it is very slow
#in a 9 by 9 there is 9^81 possible solutions
# its is very innifeicent 


#  Back tracking 
# 1. Pick empty square 
# 2. try all numbers 
# 3. find one that works 
# 4. repeat
# 5. as soon as we find out that the solution is invalid based on what we currently have we will erase the last value and go back to the previous step and bactrack repeat it
# backtrack

# this is going to be a lot faster than trying every possible combination when using backtracking we only continue with the corrrect solutions

board_1 = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


# we will need a fucntion that will pick empty squares

# we will need a for loop that tries all the numbers for each empty square 

# we need a function to find out if the number is valid

# we need a function for backtracking to go back , so we need to reset the square to 0 and go back 


def print_board(board):
    for i in range (len(board)):
        if i % 3 == 0 and i !=  0:
             print("- - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end= "")

            if j == 8 :
                print (board[i][j])
            else:
                print (str(board[i][j]) + " ", end = "")

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j



def valid(board, num, pos):
    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True

# recursive function
def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False

print_board(board_1)
solve(board_1)
print("___________________")
print_board(board_1)
