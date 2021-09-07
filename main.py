import GUI, Solver, pygame

def main():
    board_gui = GUI.Grid(GUI.WIDTH, GUI.HEIGHT, GUI.WIN, 9, 9)
    
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(GUI.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                board_gui.clicked(mouse_pos)

        GUI.draw_window(board_gui)

if __name__ == "__main__":
    main()