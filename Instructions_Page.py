import pygame
import Pygame_Button


class InstructionPage():

    def __init__(self):
        # Set up display parameters
        display_width = 800
        display_height = 800
        frames_per_second = 60

        # Set up display in game using parameters
        instructions_display = pygame.display.set_mode((display_width, display_height))
        pygame.display.set_caption('Space Invaders Game by Ning Wang')
        clock = pygame.time.Clock()
        clock.tick(frames_per_second)  # Not sure if this needs to be in the main game loop

        def instructions_menu():
            afk = 0
            timer = 0
            on_instructions_menu = True  # Keeps the game running

            # Main game loop
            while on_instructions_menu:
                instructions_display.fill((0, 0, 0))
                instructions_header = pygame.font.Font(None, 100).render('Instructions:', True, (255, 255, 0))
                instructions_display.blit(instructions_header,
                                          instructions_header.get_rect(center=(int(display_width / 2),
                                                                               int(display_height / 10))))
                instructions_subtext1 = pygame.font.Font(None, 64).render('Arrow Keys To Move', True, (255, 255, 0))
                instructions_display.blit(instructions_subtext1,
                                          instructions_subtext1.get_rect(center=(int(display_width / 2),
                                                                                int(display_height / 4))))
                instructions_subtext2 = pygame.font.Font(None, 56).render('Use Space Bar to Shoot', True, (255, 255, 0))
                instructions_display.blit(instructions_subtext2,
                                          instructions_subtext2.get_rect(center=(int(display_width / 2),
                                                                                int(3 * display_height / 8))))
                instructions_subtext3 = pygame.font.Font(None, 57).render('Press "P" Key to Pause', True, (255, 255, 0))
                instructions_display.blit(instructions_subtext3,
                                          instructions_subtext3.get_rect(center=(int(display_width / 2),
                                                                                 int(display_height / 2))))
                instructions_subtext4 = pygame.font.Font(None, 59).render('Press Escape to Close', True, (255, 255, 0))
                instructions_display.blit(instructions_subtext4,
                                          instructions_subtext4.get_rect(center=(int(display_width / 2),
                                                                                 int(5 * display_height / 8))))
                back_button = Pygame_Button.Button(instructions_display, display_width / 4, 3 * display_height / 4,
                                                   display_width / 2, display_height / 5, 'Back To Main Menu', None, 50,
                                                   0, 0, 200, 0, 0, 255, 200, 200, 0, 255, 255, 0)
                pygame.display.update()
                afk += 1
                timer += 1

                if afk >= 1800:
                    on_instructions_menu = False
                    print('You were kicked for inactivity')

                for event in pygame.event.get():
                    afk = 0
                    if event.type == pygame.QUIT:
                        on_instructions_menu = False
                    elif event.type == pygame.MOUSEBUTTONUP:
                        if back_button.over_button():
                            on_instructions_menu = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            on_instructions_menu = False

            del afk
            del timer
            del back_button
            del instructions_header
            del on_instructions_menu

        instructions_menu()
        if __name__ == '__main__':
            pygame.quit()
        else:
            del clock
            del instructions_display
            del instructions_menu


if __name__ == '__main__':
    pygame.init()
    pygame.mixer.music.load('Sounds/Falcon_vs_The_TIE_Fighters.wav')
    pygame.mixer.music.play(loops=-1)
    InstructionPage()
    quit()
