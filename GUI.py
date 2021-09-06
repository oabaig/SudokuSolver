import pygame
from Solver import example_puzzle

WIDTH, HEIGHT = 540, 630
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")

WHITE = (255,255,255)
BLACK = (0,0,0)
FPS = 60

class Grid:
    board = example_puzzle

    def __init__(self, width, height, win) -> None:
        self.rows = 9
        self.cols = 9
        self.width = width
        self.height = height
        self.win = win

    def draw_lines(self) -> None:
        for i in range(self.rows):
            if i == 0:
                continue

            horizontal_gap = self.width / 9
            vertical_gap = self.height / 9

            if i % 3 == 0 and i != 0:
                thickness = 4
            else:
                thickness = 1

            pygame.draw.line(self.win, BLACK, (i * horizontal_gap, 0), (i * horizontal_gap, self.height), thickness) # vertical lines
            pygame.draw.line(self.win, BLACK, (0, i * vertical_gap), (self.width, i * vertical_gap), thickness) # horizontal lines

class Box:
    def __init__(self) -> None:
        pass

def draw_window(board) -> None:
    WIN.fill(WHITE)

    board.draw_lines()

    pygame.display.update()
