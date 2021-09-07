import pygame
from Solver import example_puzzle

pygame.font.init() # initializes font

# START - Fonts
NUMBER_FONT = pygame.font.SysFont('comicsans', 40)
# END - Fonts

# START - Window Properties
WIDTH, HEIGHT = 540, 630
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
        
        for i in range(self.rows):
            self.boxes.append(i)
            self.boxes[i] = []
            for j in range(self.cols):
                self.boxes[i].append(Box(self.win, self.board[i][j], i, j, self.rows, self.cols,
                self.width, self.height))

    def draw_lines(self) -> None:
        for i in range(self.rows):
            if i == 0:
                continue

            horizontal_gap_offset = self.width / 9
            vertical_gap_offset = self.height / 9

            if i % 3 == 0 and i != 0:
                thickness = 4
            else:
                thickness = 1

            pygame.draw.line(self.win, BLACK, (i * horizontal_gap_offset, 0), (i * horizontal_gap_offset, self.height), thickness) # vertical lines
            pygame.draw.line(self.win, BLACK, (0, i * vertical_gap_offset), (self.width, i * vertical_gap_offset), thickness) # horizontal lines

        pygame.draw.line(self.win, BLACK, (0, self.rows * vertical_gap_offset), (self.width, self.rows * vertical_gap_offset), 4)

    def update_board(self) -> None:
        for i in range(self.rows):
            for j in range(self.cols):
                self.boxes[i][j].draw_text()

# handles boxes in board
class Box:
    def __init__(self, win, value, row, col, num_rows, num_cols, screen_width, screen_height, x_lo) -> None:
        self.win = win
        self.row = row
        self.col = col
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.value = value
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.x_offset = self.screen_width / self.num_cols
        self.y_offset = self.screen_height / self.num_rows
        print(self.row, self.col, self.value)

        if self.value == 0:
            self.usable = False
        else:
            self.usable = True

    def draw_text(self) -> None:
        if not self.usable:
            return

        horizontal_gap_offset = self.screen_width / self.num_rows
        vertical_gap_offset = self.screen_height / self.num_cols

        y_location = horizontal_gap_offset * (self.row)
        x_location = vertical_gap_offset * (self.col)

        self.value_text = NUMBER_FONT.render(str(self.value), 1, BLACK)
        self.win.blit(self.value_text, (x_location, y_location))

    def set_value(self, num) -> None:
        self.value = num
    

def draw_window(board) -> None:
    WIN.fill(WHITE)

    board.draw_lines()
    board.update_board()

    pygame.display.update()
