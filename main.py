import GUI, Solver, pygame

def main():
    board_gui = GUI.Grid(GUI.WIDTH, GUI.HEIGHT, GUI.WIN)
    
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(GUI.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        GUI.draw_window(board_gui)

if __name__ == "__main__":
    main()