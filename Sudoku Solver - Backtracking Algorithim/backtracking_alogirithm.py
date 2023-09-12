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
import pygame

board_1   =  [
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

board_processed = board_1

width_cell_config = len(board_processed[0])


# pygame initialisation 
pygame.init()
WIDTH = 700
HEIGHT = 700
CELL_COLOR = (194, 178, 128)  # Desert tan for cell backgrounds
screen = pygame.display.set_mode((700, 800))
pygame.display.set_caption("Sudoku Solver")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)



def draw_grid():
    gap = WIDTH // width_cell_config + 1 
    for i in range(width_cell_config+1):
        if i % 3 == 0:
            pygame.draw.line(screen, BLACK, (i * gap, 0), (i * gap, HEIGHT), 2)
            pygame.draw.line(screen, BLACK, (0, i * gap), (WIDTH, i * gap), 2)
        else:
            pygame.draw.line(screen, BLACK, (i * gap, 0), (i * gap, HEIGHT), 1)
            pygame.draw.line(screen, BLACK, (0, i * gap), (WIDTH, i * gap), 1)

def draw_numbers(board):
    font = pygame.font.Font(None, 36)
    cell_width = WIDTH // width_cell_config + 1
    cell_height = HEIGHT // width_cell_config + 1

    for i in range(width_cell_config):
        for j in range(width_cell_config):
            if board[i][j] != 0:
                pygame.draw.rect(screen, CELL_COLOR, (j * cell_width, i * cell_height, cell_width, cell_height))
                text = font.render(str(board[i][j]), True, BLACK)
                x = j * cell_width + cell_width // 2 - text.get_width() // 2
                y = i * cell_height + cell_height // 2 - text.get_height() // 2
                screen.blit(text, (x, y))

def draw_board(board):
    screen.fill(WHITE)  # Clear the screen with white background
    draw_grid()
    draw_numbers(board)
    pygame.display.update()


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

            if j == width_cell_config :
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

    for i in range(1,width_cell_config+1):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False


def draw_button(text, x, y, width, height, active_color, inactive_color):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screen, active_color, (x, y, width, height))

        if click[0] == 1:
            return True
    else:
        pygame.draw.rect(screen, inactive_color, (x, y, width, height))

    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.center = (x + width // 2, y + height // 2)
    screen.blit(text_surface, text_rect)
    return False




def main():
    running = True
    solving = False
    solved_board = [row[:] for row in board_processed]  # Make a copy of the original board

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)
        draw_grid()
        draw_numbers(board_processed)

        if not solving:
            if draw_button("Solve", 300, 710, 100, 50, (0, 255, 0), (0, 200, 0)):
                solving = True
                print(solve(board_processed))
                solve(solved_board)

        if solving:
            draw_board(solved_board)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()



