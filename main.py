import GUI, Solver, pygame

playable_keys = [
    pygame.K_1,
    pygame.K_2,
    pygame.K_3,
    pygame.K_4,
    pygame.K_5,
    pygame.K_6,
    pygame.K_7,
    pygame.K_8,
    pygame.K_9
]

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
            if event.type == pygame.KEYDOWN:
                if event.key in playable_keys:
                    number = playable_keys.index(event.key) + 1
                    board_gui.type_number(number)
                if event.key == pygame.K_SPACE:
                    board_gui.solve()
                

        GUI.draw_window(board_gui)

if __name__ == "__main__":
    main()