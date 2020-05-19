import pygame
import Pygame_Button
import SpaceInvadersGame
import Instructions_Page


def menu_screen(on_menu=True):
    pygame.init()
    pygame.mixer.music.load('Sounds/Falcon_vs_The_TIE_Fighters.wav')
    pygame.mixer.music.play(loops=-1)
    display_width = 800
    display_height = 800
    frames_per_second = 60

    menu_display = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('Space Invaders Clone by Ning Wang')
    clock = pygame.time.Clock()
    clock.tick(frames_per_second)

    afk = 0
    # font = pygame.font.SysFont(None, 25)
    while on_menu:
        menu_display.fill((0, 0, 0))

        main_menu_text = pygame.font.Font('freesansbold.ttf', 100).render('Star Wars', True, (255, 255, 0))
        menu_display.blit(main_menu_text,
                          main_menu_text.get_rect(center=(int(display_width / 2), int(display_height / 10))))

        main_menu_subtext = pygame.font.Font(None, 50).render('The Incomplete Ripoff', True, (255, 255, 0))
        menu_display.blit(main_menu_subtext,
                          main_menu_subtext.get_rect(center=(int(display_width / 2), int(display_height / 5))))

        main_menu_text = pygame.font.Font(None, 20).render('Programming by Ning Wang       `Voice Acting by Collin Xiao',
                                                           True, (255, 255, 0))
        menu_display.blit(main_menu_text,
                          main_menu_text.get_rect(center=(int(display_width / 2), int(24 * display_height / 25))))

        # play_button
        play_button = Pygame_Button.Button(menu_display, display_width / 4, display_height / 2,
                                           display_width / 2, display_height / 5, 'Play Game', None, 100,
                                           0, 0, 200, 0, 0, 255, 200, 200, 0, 255, 255, 0)

        instructions = Pygame_Button.Button(menu_display, display_width / 4, 3 * display_height / 4,
                                           display_width / 2, display_height / 5, 'Instructions', None, 90,
                                           0, 0, 200, 0, 0, 255, 200, 200, 0, 255, 255, 0)

        for event in pygame.event.get():
            # Exits the game via clicking the X in the corner
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.over_button():
                    SpaceInvadersGame.SpaceInvaders()
                if instructions.over_button():
                    Instructions_Page.InstructionPage()
                    pass
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    SpaceInvadersGame.SpaceInvaders()
                elif event.key == pygame.K_ESCAPE:
                    on_menu = False

        pygame.display.update()

        if afk > 10000:
            print('Closed due to afk')
            break
        afk += 1

    pygame.quit()
    quit()


if __name__ == '__main__':
    menu_screen()

