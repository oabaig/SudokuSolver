import pygame
from Solver import example_puzzle, solver

pygame.font.init() # initializes font

# START - Fonts
NUMBER_FONT = pygame.font.SysFont('comicsans', 40)
NUMBER_TYPED_FONT = pygame.font.SysFont('comicsans', 50)
# END - Fonts

# START - Window Properties
WIDTH, HEIGHT = 500, 630
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
pygame.display.set_caption("Sudoku")
# END - Window Properties

# START - Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
# END - Colors

# handles board
class Grid:
    board = example_puzzle

    def __init__(self, width, height, win, rows, cols) -> None:
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height * 0.8
        self.win = win
        self.boxes = []

        self.selected_box = None

        x_gap = self.width / self.cols
        y_gap = self.height / self.rows
        
        for i in range(self.rows):
            self.boxes.append(i)
            self.boxes[i] = []
            y_location = x_gap * i
            for j in range(self.cols):
                x_location = y_gap * j
                self.boxes[i].append(Box(self.win, self.board[i][j], i, j, x_location, y_location))

    def draw_lines(self) -> None:
        for i in range(self.rows):
            if i == 0:
                continue

            horizontal_gap_offset = self.width / self.rows
            vertical_gap_offset = self.height / self.cols

            if i % 3 == 0 and i != 0:
                thickness = 4
            else:
                thickness = 1

            pygame.draw.line(self.win, BLACK, (i * vertical_gap_offset, 0), 
                (i * vertical_gap_offset, self.width), thickness) # vertical lines
            pygame.draw.line(self.win, BLACK, (0, i * horizontal_gap_offset), 
                (self.height, i * horizontal_gap_offset), thickness) # horizontal lines

        pygame.draw.line(self.win, BLACK, (0, self.rows * horizontal_gap_offset), 
            (self.height, self.rows * horizontal_gap_offset), 4)

    def update_board(self) -> None:
        for i in range(self.rows):
            for j in range(self.cols):
                self.boxes[i][j].draw_text()

    # returns row, col based on on position clicked
    def clicked(self, pos):
        if pos[0]  < self.width and pos[1] < self.height:
            x_gap = self.width / self.cols
            y_gap = self.height / self.rows
            x = int(pos[0] // x_gap)
            y = int(pos[1] // y_gap)
            print("row:", y, "col:", x)

            if self.selected_box != None:
                self.boxes[self.selected_box[0]][self.selected_box[1]].set_selected(False)

            self.selected_box = (y,x)
            self.boxes[y][x].set_selected(True)
            return (y, x)
        else:
            return None

    def type_number(self, value):
        if self.selected_box == None:
            return

        box = self.selected_box
        self.boxes[box[0]][box[1]].set_value(value)

    def solve(self):
        solved_board = self.board
        solver(solved_board)

        for i in range(self.rows):
            for j in range(self.cols):
                self.boxes[i][j].set_value(solved_board[i][j])
        
        

# handles boxes in board
class Box:
    def __init__(self, win, value, row, col, x_location, y_location) -> None:
        self.win = win
        self.row = row
        self.col = col
        self.value = value
        self.x_location = x_location
        self.y_location = y_location
        self.selected = False

        if self.value == 0:
            self.usable = True
        else:
            self.usable = False

    def draw_text(self) -> None:
        if self.value == 0:
            return

        x_offset = 20
        y_offset = 15

        if self.usable:
            self.value_text = NUMBER_TYPED_FONT.render(str(self.value), 1, BLACK)
        else:
            self.value_text = NUMBER_FONT.render(str(self.value), 1, BLACK)
        self.win.blit(self.value_text, (self.x_location + x_offset, self.y_location + y_offset))

    def set_value(self, num) -> None:
        if self.usable:
            self.value = num

    def set_selected(self, isSelected) -> None:
        self.selected = isSelected

    def get_value(self):
        return self.value
    

def draw_window(board) -> None:
    WIN.fill(WHITE)

    board.draw_lines()
    board.update_board()

    pygame.display.update()
